# Security on Large Language Models

> To develop a handbook that empowers student developers with limited cybersecurity and LLM vulnerability knowledge to build secure chat bots confidently

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Future Work](#future-work)
- [Acknowledgements](#acknowledgements)

## Overview

This project aims to address the critical gap by developing a comprehensive Secure Chatbot Development Handbook. This handbook will be designed specifically for student developers and early stage professionals who are inexperienced in chatbot development. The handbook will aim to provide practical guidance, detailed explanation of common vulnerabilities and step-by-step implementation of secure code practices.

## Installation

All relevant installations are in requirements.txt

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

## Acknowledgements

- Created by: Koh Yihao Kendrick (U2222663K)
- Mentored by: Ong Chin Ann
