import notion
from notion.client import NotionClient

    """
    Login into notion and access to file
    Store selected lines in a list 
    Print the list to a csv file

    Returns:
        csv file with all the selected lines
    """

# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in (non-guest) session on Notion.so
client = NotionClient(token_v2="69250320efcdea81c29e141642390014d952a69875ce7d564953f84d98d7b015c285f73447500983b1aa3e175b6ece197e799ad8c0f7b5b50b5359199a725dd42f3c8ee7c2a2b4bbbd0241aaae93")
notion_page_url = "https://www.notion.so/kashishkumar/Python-test-176a5b0ba7974127916ee12311545dd9"
notion_page2_url = "https://www.notion.so/kashishkumar/Thoughts-e4ae234d7bf9463c885b549682354fb9"
def get_highlights(notion_page_url):
    notion_page = client.get_block(notion_page_url)
    thoughts_test = [child.title for child in notion_page.children]
    thoughts_new = [child.title for child in notion_page.children if len(child.title) != 0]
    selected_thoughts_new =[thought[1:] for thought in thoughts_new if thought[0]=="#"]
    return selected_thoughts_new

highlights = get_highlights(notion_page2_url) 

header = "Thoughts"
import numpy as np

def print_csv(highlights, header, filename):
    np.savetxt(filename + ".csv", highlights, delimiter=",", fmt='%s', header=header)

path=""
filename = input("What's the filename")
print_csv(highlights,header, path + filename)

