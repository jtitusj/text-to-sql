import google.generativeai as genai
import os
from ast import literal_eval
from dotenv import load_dotenv
from utils import read_textfile


def setup_model(generation_config,
                system_instructions,
                model_name="gemini-1.5-flash"):
    model = genai.GenerativeModel(
        model_name=model_name,
        generation_config=generation_config,
        system_instruction=system_instructions
    )

    return model


def initialize_validation_model(prompts_path):
    validation_prompt_file = f'{prompts_path}/validation.txt'
    system_instruction = read_textfile(validation_prompt_file)

    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 1,
        "max_output_tokens": 256,
        "response_mime_type": "text/plain",
    }

    validation_model = setup_model(generation_config, system_instruction)
    return validation_model


def validate_request(validation_model, prompt):
    response = validation_model.generate_content(prompt)
    return response


def get_metadata(response):
    metadata = {'text': response.text,
                'usage_metadata': response.usage_metadata}
    return metadata


def main():
    dotenv_path = os.path.join(os.getcwd(), '.env')
    load_dotenv(dotenv_path)

    API_KEY = os.environ.get("GOOGLE_API_KEY")

    working_dir = os.getcwd()
    prompts_path = f'{working_dir}/prompts'

    genai.configure(api_key=API_KEY)

    validation_model = initialize_validation_model(prompts_path)
    user_prompt = input("How can I help you today: ")

    validation_response = validate_request(validation_model, user_prompt)
    # validation_metadata = get_metadata(validation_response)

    print(validation_response.text)


if __name__ == '__main__':
    main()
