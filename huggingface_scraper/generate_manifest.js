import fs from 'fs'
import path, { parse } from 'path'
import prompt_sync from 'prompt-sync'
import prompt_sync_history from 'prompt-sync-history'
import hf_embed_calc from './manifests/manifest_hf_embed.js'
import llama_cpp_calc from './manifests/manifest_llama_cpp.js'
import hf_lm_calc from './manifests/manifest_hf_lm.js'
import hf_t5_calc from './manifests/manifest_hf_t5.js'
import knn_calc from './manifests/manifest_knn.js'
import api_calc from './manifests/manifest_api.js'
import hf_faster_whisper_calc from './manifests/manifest_hf_faster_whisper.js'
import hf_transformers_calc from './manifests/manifest_hf_transformers.js'
import diffusion_calc from './manifests/manifest_diffusion.js'
import {complete, parse_templates, generate_test} from './utils.js'

export class Generate_Manifest{
    constructor(){
        this.metadata = {}
        this.hwRequirements = {}
    }

    main(generate){
        let self = this
        let generation = self.generate(generate)
        return generation
    }

    generate(generate){
        let self = {}
        let metadata = self.metadata
        let hwRequirements = self.hwRequirements
        let results
        let model_types = ['hf_transformers', 'hf_embed', 'llama_cpp', 'diffusion', 'knn', 'api', 'whisper', 'custom']
        // prompt the user for input
        console.log("1. hf_transformers")
        console.log("2. hf_embed")
        console.log("3. llama_cpp")
        console.log("4. diffusion")
        console.log("5. knn")
        console.log("6. api")
        console.log("7. whisper")
        console.log("8. custom")
        // request console input
        let prompt = prompt_sync(({
            history: prompt_sync_history(),
            autocomplete: complete(model_types),
            sigint: true
        }))
    
        let model_type = prompt("Select a model type: ")
        // check if the input is valid
        console.log("confirm model type: " + model_type)
        if (!model_types.includes(model_type)){
            if (parseInt(model_type) > 0 && parseInt(model_type) < 8){
                model_type = model_types[parseInt(model_type) - 1]
            }
            else{
                console.log("Invalid model type")
                return
            }
        }
    
        self.skill = model_type
    
        if (model_type == 'hf_transformers'){
            results = hf_transformers_calc(self)
        }

        if (model_type == 'hf_faster_whisper'){
            results = hf_faster_whisper_calc(self)
        }

        if (model_type == 'hf_lm'){
            results = hf_lm_calc(self)
        }

        if (model_type == "hf_t5"){
            results = hf_t5_calc(self)
        }
    
        if (model_type == 'hf_embed'){
            results = hf_embed_calc(self)
        }
    
        if (model_type == 'llama_cpp'){
            results = llama_cpp_calc(self)
        }
    
        if (model_type == 'diffusion'){
            results = diffusion_calc(self)
        }
    
        if (model_type == 'knn'){
            results = knn_calc(self)
        }
    
        if (model_type == 'api'){
            results = api_calc(self)
        }
    
        if (model_type == 'custom'){
            results = custom_calc(self)
        }

        try{
            test = generate_test(results)
        }
        catch(err){
            console.log(err)
            throw("Error in testing the manifest " +  model_type)
    
        }
        finally{
            return results
        }
    
    }
    
    custom_calc(self){
        throw("custom is not yet supported")
    }

}
