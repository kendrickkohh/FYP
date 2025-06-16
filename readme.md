# Security on Large Language Models

> To develop a handbook that empowers student developers with limited cybersecurity and LLM vulnerability knowledge to build secure chat bots confidently

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Future Work](#future-work)
- [Acknowledgements](#acknowledgements)

## Overview

This project aims to address the critical gap by developing a comprehensive Secure Chatbot Development Handbook. This handbook will be designed specifically for student developers and early stage professionals who are inexperienced in chatbot development. The handbook will aim to provide practical guidance, detailed explanation of common vulnerabilities and step-by-step implementation of secure code practices.

## Current Modules / Project Components

`get_embedding.py`  
Handles embedding generation using the `mxbai-embed-large` model.

`guardrail.py`  
Implements [LLM Guard](https://github.com/protectai/llm-guard) to sanitize and validate both inputs and outputs from the LLM.

`populate_database.py`  
Populates the vector datastore by:
- Checking the `data/` folder for new entries
- Adding any new data into the datastore if not already present

`query_data.py`  
Main querying interface that:
- Accepts user queries and sends them to the LLM
- Uses RAG (Retrieval-Augmented Generation) to retrieve relevant context from the datastore
- Applies input/output validation using `guardrail.py`

`Ollama models`
Llama3.2

## Installation

- All relevant installations are in requirements.txt
- Note that we use `python3.10` to run the programs

```bash
pip install -r requirements.txt
source ./venv/bin/activate
```

## Future work

- Implement security and domain folders, as we embed information, the data is categorised in its metadata. This way we can call them indifferently when querying the model.
- This will be done in `populate_database.py`

```bash
for doc in docs:
    path = doc.metadata.get("source", "").lower()
    if "/security/" in path:
        doc.metadata["category"] = "security"
    elif "/domain/" in path:
        doc.metadata["category"] = "domain"
```

- Similarity search
- This will be done in `query_data.py`

```bash
security_results = db.similarity_search_with_score(query_text, k=3, filter={"category": "security"})
domain_results = db.similarity_search_with_score(query_text, k=5, filter={"category": "domain"})
```

- Look into producing malicious data for images and audio
- How to generate a malicious image: `https://www.youtube.com/watch?v=dqdOJzzWxs4`

## Acknowledgements

- Created by: Koh Yihao Kendrick (U2222663K)
- Mentored by: Ong Chin Ann
