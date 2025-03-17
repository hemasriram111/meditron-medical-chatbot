## Ayushmana: AI in Health Care 🏥

Ayushmana is an AI-powered healthcare chatbot that leverages a local Meditron LLM and Google Gemini Vision API to assist users with medical queries and prescription analysis.

## Features
- **Medical AI Chatbot**: Uses Meditron LLM to answer healthcare-related questions.
- **Prescription Analysis**: Extracts text from uploaded prescription images using Google Gemini Vision API.
- **Interactive Chat Interface**: Allows users to ask medical queries and receive AI-generated responses.
- **Contextual Understanding**: Integrates extracted prescription data with user queries for more relevant answers.
- **User-Friendly UI**: Built using Streamlit for a smooth and intuitive experience.

## Technologies Used
- **Streamlit**: For creating the web interface.
- **Ollama**: To run the local Meditron LLM.
- **Google Gemini AI**: For processing prescription images.
- **Pillow (PIL)**: To handle image uploads.
- **Python**: Core language for backend logic.

## Installation & Setup
1. Clone the repository:
   ```bash
   git clone https: https://github.com/hemasriram111/meditron-medical-chatbot.git
   cd meditron-medical-agent
   ```
2. Install dependencies:
   ```bash
   pip install streamlit ollama google-generativeai pillow
   ```
3. Configure Google Gemini API key:
   - Replace `GEMINI_API_KEY` in the script with your actual API key.
4. Start the Ollama Meditron LLM:
   ```bash
   ollama serve
   ```
5. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Usage
- Start the application and interact with the chatbot.
- Toggle **Prescription Analysis** to enable image-based text extraction.
- Upload a medical prescription image (JPG, PNG) for processing.
- Ask any healthcare-related questions, and the AI will provide responses.

## Disclaimer
⚠️ *This application is for informational purposes only. It does not provide medical advice. Always consult a healthcare professional for medical concerns.*

## Future Enhancements
- Improve accuracy of prescription data extraction.
- Add multilingual support for medical queries.
- Implement integration with electronic health records (EHRs).

## Contributing
Feel free to contribute by submitting pull requests or reporting issues.

## License
This project is licensed under the MIT License.

