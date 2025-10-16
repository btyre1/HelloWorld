import gradio as gr

# Define a simple function
def greet(name):
    return f"Hello {name}!"

# Create the interface
iface = gr.Interface(
    fn=greet,           # The function to wrap
    inputs="text",      # Input type
    outputs="text"      # Output type
)

# Launch the app
iface.launch()