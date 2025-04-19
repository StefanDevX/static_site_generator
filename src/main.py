from textnode import TextNode, TextType

print("hello world")

def main():
    dummy = TextNode("Just a text", TextType.TEXT, "http://boot.dev")
    print(dummy)

if __name__ == "__main__":
    main()
