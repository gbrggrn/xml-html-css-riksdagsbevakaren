# Riksdagsbevakaren - Informationsguide

## Context

* **Origin** Developed as part of an XML-course.
* **Objective** To fetch data from Riksdagens open API, transform via XQuery and present in HTML through XSLT.
* **Status** 🟢 Complete/Functional

---

## Systems Architecture

* **Logic** Python-scripted fetching + XML + XQuery + XSLT + XPath + CSS
* **Tech Stack** XML-Tools + Saxon HE (XQuery engine) + Python dev server

---

## Functionality

* Fetch staff/votes/docs via Python scripts from Riksdagens open API
* Transform raw XML files to usable datamodels
* Navigate through staff to explore:
 - What official positions they have held
 - Their five latest motions (docs)
 - How they cast their latest ten latest votes
* All docs have source links

---

## Setup & Usage

Based on usage in VSCode + java + venv installed
1. Clone the repository
2. Download the Saxon HE .jar and place it in the root folder
3. Add the XML-Tools extension to VSCode
4. Run the python scripts from the root directory:
 - 1. py extract/fetch_staff.py
 - 2. py extract/fetch_docs.py
 - 3. py extract/fetch_votes.py
5. Run the three XQueries from the transform folder and keep the standard out-filename:
 - ctrl+shift+p: XML-Tools Execute XQuery
6. Spin up the Python dev server:
 - py -m http.server 8000
7. Navigate to http://localhost:8000/main.xml

---

## Learning Outcomes

* Navigating through XML-structures using XPath
* Transforming XML -> HTML via XSLT
* Validating XML through DTD and XML-schema
* Styling XML via CSS
* Creating vector based graphics (SVG-files) with XML
* Data modeling and transformation through XQuery