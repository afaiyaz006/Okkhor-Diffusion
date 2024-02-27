from diffusers import DiffusionPipeline
from typing import List, Optional, Tuple, Union
import torch
import gradio as gr
css="""
#input-panel{
align-items:center;
justify-content:center
    
}
"""
modelnames=[
    "ahmedfaiyaz/OkkhorDiffusion",
    "ahmedfaiyaz/OkkhorDiffusion-CMATERdb",
    "ahmedfaiyaz/OkkhorDiffusion-Ekush"
]
current_model="ahmedfaiyaz/OkkhorDiffusion"
#updated username
pipeline = DiffusionPipeline.from_pretrained(current_model,custom_pipeline="ahmedfaiyaz/OkkhorDiffusion",embedding=torch.float16)
character_mappings = {
    'অ': 1,
    'আ': 2,
    'ই': 3,
    'ঈ': 4,
    'উ': 5,
    'ঊ': 6,
    'ঋ': 7,
    'এ': 8,
    'ঐ': 9,
    'ও': 10,
    'ঔ': 11,
    'ক': 12,
    'খ': 13,
    'গ': 14,
    'ঘ': 15,
    'ঙ': 16,
    'চ': 17,
    'ছ': 18,
    'জ': 19,
    'ঝ': 20,
    'ঞ': 21,
    'ট': 22,
    'ঠ': 23,
    'ড': 24,
    'ঢ': 25,
    'ণ': 26,
    'ত': 27,
    'থ': 28,
    'দ': 29,
    'ধ': 30,
    'ন': 31,
    'প': 32,
    'ফ': 33,
    'ব': 34,
    'ভ': 35,
    'ম': 36,
    'য': 37,
    'র': 38,
    'ল': 39,
    'শ': 40,
    'ষ': 41,
    'স': 42,
    'হ': 43,
    'ড়': 44,
    'ঢ়': 45,
    'য়': 46,
    'ৎ': 47,
    'ং': 48,
    'ঃ': 49,
    'ঁ': 50,
    '০': 51,
    '১': 52,
    '২': 53,
    '৩': 54,
    '৪': 55,
    '৫': 56,
    '৬': 57,
    '৭': 58,
    '৮': 59,
    '৯': 60,
    'ক্ষ(ksa)': 61,
    'ব্দ(bda)': 62,
    'ঙ্গ': 63,
    'স্ক': 64,
    'স্ফ': 65,
    'স্থ': 66,
    'চ্ছ': 67,
    'ক্ত': 68,
    'স্ন': 69,
    'ষ্ণ': 70,
    'ম্প': 71,
    'হ্ম': 72,
    'প্ত': 73,
    'ম্ব': 74,
    'ন্ড': 75,
    'দ্ভ': 76,
    'ত্থ': 77,
    'ষ্ঠ': 78,
    'ল্প': 79,
    'ষ্প': 80,
    'ন্দ': 81,
    'ন্ধ': 82,
    'ম্ম': 83,
    'ন্ঠ': 84,
}
ekush_mappings = {
    'অ': 0,
    'আ': 1,
    'ই': 2,
    'ঈ': 3,
    'উ': 4,
    'ঊ': 5,
    'ঋ': 6,
    'এ': 7,
    'ঐ': 8,
    'ও': 9,
    'ঔ': 10,
    'ক': 11,
    'খ': 12,
    'গ': 13,
    'ঘ': 14,
    'ঙ': 15,
    'চ': 16,
    'ছ': 17,
    'জ': 18,
    'ঝ': 19,
    'ঞ': 20,
    'ট': 21,
    'ঠ': 22,
    'ড': 23,
    'ঢ': 24,
    'ণ': 25,
    'ত': 26,
    'থ': 27,
    'দ': 28,
    'ধ': 29,
    'ন': 30,
    'প': 31,
    'ফ': 32,
    'ব': 33,
    'ভ': 34,
    'ম': 35,
    'য': 36,
    'র': 37,
    'ল': 38,
    'শ': 39,
    'ষ': 40,
    'স': 41,
    'হ': 42,
    'ড়': 43,
    'ঢ়': 44,
    'য়': 45,
    'ৎ': 46,
    'ং': 47,
    'ঃ': 48,
    'ঁ': 49,
    'ব্দ': 50,
    'ঙ্গ': 51,
    'স্ক': 52,
    'স্ফ': 53,
    'চ্ছ': 54,
    'স্থ': 55,
    'ক্ত': 56,
    'স্ন': 57,
    'ষ্ণ': 58,
    'ম্প': 59,
    'প্ত': 60,
    'ম্ব': 61,
    'ত্থ': 62,
    'দ্ভ': 63,
    'ষ্ঠ': 64,
    'ল্প': 65,
    'ষ্প': 66,
    'ন্দ': 67,
    'ন্ধ': 68,
    'স্ম': 69,
    'ণ্ঠ': 70,
    'স্ত': 71,
    'ষ্ট': 72,
    'ন্ম': 73,
    'ত্ত': 74,
    'ঙ্খ': 75,
    'ত্ন': 76,
    'ন্ড': 77,
    'জ্ঞ': 78,
    'ড্ড': 79,
    'ক্ষ': 80,
    'দ্ব': 81,
    'চ্চ': 82,
    'ক্র': 83,
    'দ্দ': 84,
    'জ্জ': 85,
    'ক্ক': 86,
    'ন্ত': 87,
    'ক্ট': 88,
    'ঞ্চ': 89,
    'ট্ট': 90,
    'শ্চ': 91,
    'ক্স': 92,
    'জ্ব': 93,
    'ঞ্জ': 94,
    'দ্ধ': 95,
    'ন্ন': 96,
    'ঘ্ন': 97,
    'ক্ল': 98,
    'হ্ন': 99,
    '০': 100,
    '১': 101,
    '২': 102,
    '৩': 103,
    '৪': 104,
    '৫': 105,
    '৬': 106,
    '৭': 107,
    '৮': 108,
    '৯': 109
}

cmaterdb_mappings = {
    'প্র': 0,
    'ঙ্গ': 1,
    'ক্ষ': 2,
    'ত্র': 3,
    'ন্দ': 4,
    'চ্ছ': 5,
    'ন্ত': 6,
    'ন্দ্র': 7,
    'স্ত': 8,
    'ন্তু': 9,
    'গ্র': 10,
    'স্থ': 11,
    'স্ট': 12,
    'ম্ব': 13,
    'স্ব': 14,
    'ত্ত': 15,
    'ক্ত': 16,
    'ন্ট': 17,
    'ল্প': 18,
    'ষ্ট': 19,
    'ন্ত্র': 20,
    'ক্র': 21,
    'ন্ন': 22,
    'দ্ধ': 23,
    'ন্ধ': 24,
    'ঙ্ক': 25,
    'ন্ড': 26,
    'ফ্র': 27,
    'ম্প': 28,
    'স্ক': 29,
    'জ্ঞ': 30,
    'ক্ট': 31,
    'শ্চ': 32,
    'ট্র': 33,
    'ত্ব': 34,
    'ল্ল': 35,
    'ব্র': 36,
    'ঞ্চ': 37,
    'ণ্ড': 38,
    'ক্স': 39,
    'শ্র': 40,
    'দ্র': 41,
    'স্প': 42,
    'ঞ্জ': 43,
    'ন্স': 44,
    'ম্ভ': 45,
    'শ্ব': 46,
    'ব্দ': 47,
    'শ্ন': 48,
    'প্প': 49,
    'ব্ল': 50,
    'প্ত': 51,
    'ক্ল': 52,
    'ষ্ট্র': 53,
    'দ্ব': 54,
    'ট্ট': 55,
    'গ্ল': 56,
    'ল্ট': 57,
    'ষ্ঠ': 58,
    'স্ত্র': 59,
    'প্ল': 60,
    'চ্চ': 61,
    'স্ম': 62,
    'দ্দ': 63,
    'গ্ন': 64,
    'জ্ব': 65,
    'ষ্ক': 66,
    'ত্ম': 67,
    'ড্র': 68,
    'ম্ম': 69,
    'ণ্ট': 70,
    'ম্প্র': 71,
    'প্ন': 72,
    'ন্ম': 73,
    'স্ফ': 74,
    'ল্দ': 75,
    'ত্ত্ব': 76,
    'জ্জ': 77,
    'ক্ষ্ম': 78,
    'ষ্ণ': 79,
    'ন্ব': 80,
    'ক্ক': 81,
    'ন্থ': 82,
    'ড্ড': 83,
    'ব্ব': 84,
    'ন্ট্র': 85,
    'ণ্ঠ': 86,
    'প্ট': 87,
    'স্তু': 88,
    'ধ্ব': 89,
    'হ্ণ': 90,
    'ভ্র': 91,
    'ল্ক': 92,
    'স্ল': 93,
    'হ্ন': 94,
    'ত্ন': 95,
    'ষ্ক্র': 96,
    'ঘ্র': 97,
    'দ্ভ': 98,
    'শ্ল': 99,
    'ব্ধ': 100,
    'ষ্ম': 101,
    'স্ক্র': 102,
    'ড়্গ': 103,
    'জ্জ্ব': 104,
    'শ্ম': 105,
    'দ্ম': 106,
    'ক্ব': 107,
    'ম্র': 108,
    'গ্ধ': 109,
    'ব্জ': 110,
    'স্ন': 111,
    'ন্দ্ব': 112,
    'হ্ম': 113,
    'ঙ্ঘ': 114,
    'খ্র': 115,
    'ত্থ': 116,
    'ল্ব': 117,
    'ম্ন': 118,
    'ঘ্ন': 119,
    'গ্গ': 120,
    'ক্ষ্ণ': 121,
    'গ্রু': 122,
    'চ্ছ্ব': 123,
    'ণ্ণ': 124,
    'ল্ম': 125,
    'স্র': 126,
    'ম্ল': 127,
    'ষ্প্র': 128,
    'ঞ্ঝ': 129,
    'স্প্র': 130,
    'ম্ভ্র': 131,
    'ষ্প': 132,
    'ঙ্খ': 133,
    'জ্র': 134,
    'গ্ব': 135,
    'থ্ব': 136,
    'ণ্ব': 137,
    'হ্ব': 138,
    'দ্দ্ব': 139,
    'দ্ঘ': 140,
    'ধ্র': 141,
    'হ্ল': 142,
    'গ্ম': 143,
    'ল্গ': 144,
    'স্খ': 145,
    'থ্র': 146,
    'ন্ধ্র': 147,
    'ন্দ্ব': 148,
    'ফ্ল': 149,
    'ঙ্ক্ষ': 150,
    'ণ্ম': 151,
    'ঞ্ছ': 152,
    'ম্ফ': 153,
    'হ্র': 154,
    'প্রু': 155,
    'ত্রু': 156,
    'ভ্ল': 157,
    'শ্রু': 158,
    'দ্রু': 159,
    'ঙ্ম': 160,
    'ক্ম': 161,
    'দ্গ': 162,
    'ন্ড্র': 163,
    'ট্ব': 164,
    'চ্ঞ': 165,
    'প্স': 166,
    'ল্ড': 167,
    'ষ্ফ': 168,
    'শ্ছ': 169,
    'জ্ঝ': 170,
    'স্ট্র': 171,
    'অ': 172,
    'আ': 173,
    'ই': 174,
    'ঈ': 175,
    'উ': 176,
    'ঊ': 177,
    'ঋ': 178,
    'এ': 179,
    'ঐ': 180,
    'ও': 181,
    'ঔ': 182,
    'ক': 183,
    'খ': 184,
    'গ': 185,
    'ঘ': 186,
    'ঙ': 187,
    'চ': 188,
    'ছ': 189,
    'জ': 190,
    'ঝ': 191,
    'ঞ': 192,
    'ট': 193,
    'ঠ': 194,
    'ড': 195,
    'ঢ': 196,
    'ণ': 197,
    'ত': 198,
    'থ': 199,
    'দ': 200,
    'ধ': 201,
    'ন': 202,
    'প': 203,
    'ফ': 204,
    'ব': 205,
    'ভ': 206,
    'ম': 207,
    'য': 208,
    'র': 209,
    'ল': 210,
    'শ': 211,
    'ষ': 212,
    'স': 213,
    'হ': 214,
    'ড়': 215,
    'ঢ়': 216,
    'য়': 217,
    'ৎ': 218,
    'ং': 219,
    'ঃ': 220,
    'ঁ': 221
}
character_mappings_model_wise={
    "ahmedfaiyaz/OkkhorDiffusion":character_mappings,
    "ahmedfaiyaz/OkkhorDiffusion-CMATERdb":cmaterdb_mappings,
    "ahmedfaiyaz/OkkhorDiffusion-Ekush":ekush_mappings
}



def generate(modelname:str,input_text:str,batch_size:int,inference_steps:int):
    batch_size=int(batch_size)
    inference_steps=int(inference_steps)
    print(f"Generating image with label:{character_mappings[input_text]} batch size:{batch_size}")
    label=int(character_mappings_model_wise[current_model][input_text])
    pipeline.embedding=torch.tensor([label])
    generate_image=pipeline(batch_size=batch_size,num_inference_steps=inference_steps).images
    return generate_image


def switch_pipeline(modelname:str):
    global pipeline
    pipeline = DiffusionPipeline.from_pretrained(modelname,custom_pipeline="ahmedfaiyaz/OkkhorDiffusion",embedding=torch.float16)
    global current_model
    current_model=modelname
    return f"""
            <div style="text-align: center; margin: 0 auto;">Selected model <a href="https://huggingface.com/models/{modelname}">{modelname}</a></div>
            """,gr.update(choices=character_mappings_model_wise[modelname])


with gr.Blocks(css=css,elem_id="panel") as od_app:
    with gr.Column(min_width=100):
        text=gr.HTML("""
         <div style="text-align: center; margin: 0 auto;">
              <div style="display: inline-flex;align-items: center;gap: 0.8rem;font-size: 1.75rem;">
                <h1> Okkhor Diffusion </h1>
               </div>
        </div>
""")
    #input panel 
    choosen_model=gr.HTML(f"""
                          <div style="text-align: center; margin: 0 auto;">Selected model <a href="https://huggingface.com/models/{current_model}">{current_model}</a></div>
                          """)
    with gr.Row(elem_id="input-panel"):

        with gr.Column(variant="panel",scale=0,elem_id="input-panel-items"):
            choose_model=gr.Dropdown(label="Select model",choices=modelnames,value=modelnames[0])
            dropdown = gr.Dropdown(label="Select Character",choices=list(character_mappings_model_wise[current_model].keys()))
            batch_size = gr.Number(label="Batch Size", minimum=0, maximum=100)
            inference_steps= gr.Slider(label="Steps",value=100,minimum=100,maximum=1000,step=100)

            btn = gr.Button("Generate",size="sm")  
      
        
    gallery = gr.Gallery(
        label="Generated images", show_label=False, elem_id="gallery"
    , columns=[10], rows=[10], object_fit="contain", height="auto",scale=1,min_width=80)

    choose_model.change(fn=switch_pipeline,inputs=[choose_model],outputs=[choosen_model,dropdown]) 
    btn.click(fn=generate,inputs=[choose_model,dropdown,batch_size,inference_steps],outputs=[gallery])
    
if __name__=='__main__':
    od_app.queue(max_size=20).launch(show_error=True)
