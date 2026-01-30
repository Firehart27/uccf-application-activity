# uccf-application-activity
Public repository for the completion of the assigned activity for the digital systems developer application by UCCF: A data visualisation tool built with **Python** and **Dash** to map and explore Christian Unions across the UK using the API link provided.

## Assignment Parameters
Language: Python
API link: https://v1.data.uccf.io/api/christian-unions/expand

## Installation & Setup
1. Clone the repository
```bash
git clone [YOUR_REPO_URL]
cd [YOUR_REPO_NAME]
```
2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Run the application
```bash
python main.py
```
Once the script is ran, the terminal will provide a local link to view the application.


## Task Approach Brief
I used Jupyter Notebooks for interactive development as well as decided to use Python as I am familiar with it and somewhat familiar with using plotly.
I loaded the API data and displayed it to decide the prioritisation of information.

I decided that displaying the Christian Unions (CU) on a map of the UK was most user friendly as users will most likely be students or family or churches who would be more familiar with the location over the exact name of the CU or the exact name of the University.
I also decided that if it is possible, to have the details of the websites and social media links to be prioritised as they would be the main way people would connect with the CU or discover CU events.

I implemented this plan using Dash framework as I was familiar with using plotly for my previous projects.
I found templates for using Scattermaps from youtube videos and Dash's own website documentation as well.
I used generative AI (claude and gemini) to synthesise the newly learnt information as well as to aid development by debugging kinks produced by my own clumsiness using a new tool.

After verifying it works using Jupyter Notebooks, I moved the important code to main.py.
I ran main.py in a virtual environment to A. ensure it works and B. extract the minimum requirements to be stored in requirements.txt

### Robustness
The code was tested in a fresh virtual environment, as such it would mean it should run on most devices with the requirements installed.

Since this is a proof of concept type project, the data processing could be done in a seperate file to improve code sanitisation.
Furthermore, further sanitisation steps could be done to defend against injection attacks.

### Future Development
I would have to fix the CUs with no geolocation. As the temporary fix was to send them into 0, 0 in coordinates, while a permanent fix would be investigated (such as having a fallback geolocation using open source maps).

I would also try to think about how to better understand the purpose of the ID and how to better use the naming of the CU for easier acces.
A search function would aid people with limited geographical knowledge of the UK (i.e. international students).