# Ask Your PDF

This repository contains the code for a Streamlit app that allows you to ask questions about a PDF document. The app uses the OpenAI GPT-3.5-turbo language model to generate answers to your questions.

## Getting Started

1. Clone this GitHub repository or download the zip for this project.

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set you OPENAI API key:
   If you wish to run this app locally, then add your `OPENAI_API_KEY` to your system's environment variable. [Learn more](https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety).

   *Alternatively*:
   - Create a file `apikey.py` in same directory as `app.py`
   - Input your OPENAI_API_KEY in the `api_key.py`.
   - For example: `OPENAI_API_KEY = 'xx-xxxxxxxxxxxxxxxxxYOUR_API_KEYxxxxxxxxxxxxxxxxxxx'`
   - And add these two lines in your `app.py` and `scrapper.py`

    ```python
    from apikey import OPENAI_API_KEY
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
    ```

    > [!IMPORTANT]
    > Make sure to add `apikey.py` to your `.gitignore` file to avoid exposing your API key.

4. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

    Your application should be live on <http://localhost:8501/>

The application will open a web page in your browser. You can then upload a PDF document to the application and ask questions about it. The application will generate text responses to your questions with regards to your uploaded PDF document.

For each query, you will also be showcased the API call charges.

> [!IMPORTANT]
> The `OpenAIEmbeddings` and response generations are chargable by the OPENAI API Key. To avoid unnecessary charges, I would recommend you use the [`A_Deep_Learning_Approach_for_Text_Generation.pdf`](A_Deep_Learning_Approach_for_Text_Generation.pdf) file for testing, since its corresponding [`.pkl`](A_Deep_Learning_Approach_for_Text_Generation.pkl) file is ready to use.

![Screenshot of application](/screenshot.jpeg)

## Usage

1. Upload a PDF document to the app.
2. Enter your question in the text box.
3. Hit enter

The app will generate an answer to your question.

## My Takeaways

- How to use the OpenAI API to generate text responses.
- How to use the PyPDF2 library to read and parse PDF documents.
- How to use the FAISS library to create and search a vector store.
- How to use the langchain library to build a question answering chain.
- How to optimize the performance of a question answering chain by caching the embeddings of the PDF documents.

## File Structure

The file structure of the repository is as follows:

```
.
├── .gitignore
├── README.md
├── A_Deep_Learning_Approach_for_Text_Generation.pdf
├── Al_Text_Generators_and_Text_Producers.pdf
├── A_Deep_Learning_Approach_for_Text_Generation.pkl
├── apikey.py
├── app.py
└── requirements.txt
```

The `.gitignore` file specifies the files that should be ignored by Git.

The `README.md` file is the project README.

The `*.pdf` files are the PDF documents that you can upload to the app.

The `*.pkl` file is a pickled object that stores the embeddings of the PDF documents.

The `apikey.py` file contains the OpenAI API key.

The `app.py` file is the main file for the Streamlit app.

The `requirements.txt` file lists the Python packages that are required to run the app.

## Contributing

Contributions are welcome! Please open a pull request if you have any suggestions, improvements or bug fixes.

### Contact me

Feel free to reachout to me for suggestions, collaboration, or community via:

<a href="https://github.com/SaifuddinSaifee" target="_blank">
<img src=https://img.shields.io/badge/github-%2324292e.svg?&style=for-the-badge&logo=github&logoColor=white alt=github style="margin-bottom: 5px;" />
</a>
<a href="https://twitter.com/SaifSaifee_dev" target="_blank">
<img src=https://img.shields.io/badge/twitter-%2300acee.svg?&style=for-the-badge&logo=twitter&logoColor=white alt=twitter style="margin-bottom: 5px;" />
</a>
<a href="https://dev.to/saifuddinsaifee" target="_blank">
<img src=https://img.shields.io/badge/dev.to-%2308090A.svg?&style=for-the-badge&logo=dev.to&logoColor=white alt=devto style="margin-bottom: 5px;" />
</a>
<a href="https://linkedin.com/in/saifuddinsaifee" target="_blank">
<img src=https://img.shields.io/badge/linkedin-%231E77B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white alt=linkedin style="margin-bottom: 5px;" />
</a>
