from langchain_community.llms import LlamaCpp
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler

def load_model():
    callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

    return LlamaCpp(
        model_path="models/dolphin.gguf",
        n_ctx=2048,
        temperature=0,
        max_tokens=2000,
        top_p=1,  
        callback_manager=callback_manager,
        verbose=True, 
    
    )

