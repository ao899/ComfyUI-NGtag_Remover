class NGtag_Remover:
    @classmethod
    def INPUT_TYPES(s):
                return {"required": 
                { 
                    "input_string": ("STRING", {"forceInput": True}),
                    "NGtag1": ("STRING", {"forceInput": False}),                  
                    "NGtag2": ("STRING", {"forceInput": False}),
                    "NGtag3": ("STRING", {"forceInput": False}),
                    "NGtag4": ("STRING", {"forceInput": False}),
                    "NGtag5": ("STRING", {"forceInput": False}),
                    "NGtag6": ("STRING", {"forceInput": False}),
                    "NGtag7": ("STRING", {"forceInput": False}),
                    "NGtag8": ("STRING", {"forceInput": False}),
                }
                }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("output_string",)
    FUNCTION = "run"
    CATEGORY = "Personal Utils"
 
    def run( self, input_string, NGtag1, NGtag2, NGtag3, NGtag4, NGtag5, NGtag6, NGtag7, NGtag8 ):

        ng_tag = [""] * 9  
        ng_tag[1] = NGtag1.strip().replace("\n", "")
        ng_tag[2] = NGtag2.strip().replace("\n", "")
        ng_tag[3] = NGtag3.strip().replace("\n", "")
        ng_tag[4] = NGtag4.strip().replace("\n", "")
        ng_tag[5] = NGtag5.strip().replace("\n", "")
        ng_tag[6] = NGtag6.strip().replace("\n", "")
        ng_tag[7] = NGtag7.strip().replace("\n", "")
        ng_tag[8] = NGtag8.strip().replace("\n", "")

        output_prompt = ""
        prompt = input_string.split(',')
        num_of_tags = len( prompt )
        for i in range( num_of_tags ):
            prompt[i] = prompt[i].strip()
            found_ng_tag = False
            for j in range( 1, 9 ):
                if ng_tag[j] == "":
                    pass
                else:
                    if ng_tag[j] in prompt[i]:
                        found_ng_tag = True
                        break
                    else:
                        pass
            if found_ng_tag == True:
                pass
            else:
                output_prompt = output_prompt + prompt[i] + ", "
        return (output_prompt.rstrip(', '),)

NODE_CLASS_MAPPINGS = {
    "NGtag_Remover": NGtag_Remover,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "NGtag_Remover": "NGtag_Remover",
}