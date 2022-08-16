import sys

def parse_collaborators():
    try:
        collaborators = sys.argv[1]
        print(collaborators)
    except:
        print("Failed to parse collaborators")

if __name__ == 'main':
    print ("1223")
    parse_collaborators()
