from typing import Annotated
from typing_extensions import TypedDict
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
import asyncio

class State(TypedDict):
    messages: Annotated[list, add_messages]


graph_builder = StateGraph(State)
llm = ChatOllama(model="llama3.2:latest")


def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}

# Define the node in the graph
graph_builder.add_node("chatbot", chatbot)
graph_builder.set_entry_point("chatbot")
graph_builder.set_finish_point("chatbot")
graph = graph_builder.compile()

def make_graph():   
    try:
        # Get the binary image data from the graph in PNG format
        image_data = graph.get_graph().draw_mermaid_png()
        # Write the binary image data to a file
        with open("graph_image.png", "wb") as file:
            file.write(image_data)

        print("Graph image saved to 'graph_image.png'")
    except Exception as e:
        print("An error occurred:", e)

# Change to async generator
async def stream_graph_updates(user_input: str):
    loop = asyncio.get_event_loop()
    for event in await loop.run_in_executor(None, lambda: graph.stream({"messages": [("user", user_input)]})):
        for value in event.values():
            if isinstance(value, dict) and "messages" in value:
                yield value["messages"][-1].content
            else:
                yield "Unexpected response format"
    