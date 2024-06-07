import markdown_to_json as mdj
import requests

def md_to_json():
    with open("home.md", "r") as f:
        content = f.read()
        data = mdj.dictify(content)
        title =data['Main']['Hero']['Title'][0]
        description = data['Main']['Hero']['Description'][0]
        button = data['Main']['Hero']['Button'][0]
        hero = {
            'title': title, 
            'description': description, 
            'button': button,
            'id': 1
        }
        about = {
            'title': 'About Us',
            'description': data['About']['About']['About'][0],
            'highlight_text': data['About']['About']['Highlight'][0],
            'year': data['About']['About']['Year'][0],
            'mission_text': data['About']['About']['Mission'][0],
            'vision_text': data['About']['About']['Vision'][0],
            'values_text': 'N/A',
            'id': 1
        }
        data = {
            'hero': hero,
            'about': about
        }
        return data

def send_request(data):
    url = "http://localhost:8000/api/v1/edit-page/"
    payload = {
        'data' : data
    }
    response = requests.put(url, json=payload)
    if response.status_code == 200:
        print("Updated successfully.")
    else:
        print("An error occurred.")


def main():
    data = md_to_json()
    send_request(data)

if __name__ == "__main__":
    main()
