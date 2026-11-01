from fastapi import FastAPI, Body
from ollama import Client

app = FastAPI()
client = Client(host="http://localhost:11434")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/chat")
def chat(message: str = Body(..., example="Hello, how are you?")):
    response = client.chat(
        model="gemma2:2b",
        messages=[{"role": "user", "content": message}],
    )
    return {"response": response.message.content}

## ask about fill form of api 
# here is o/p form swagger ui 
# {
#   "response": "It seems you're asking about APIs and their \"full potential.\" 
#  Let's dive into what that means.\n\n**What is an API?**\n\nAn API, or Application Programming Interface, is a software intermediary that lets two different pieces of software talk to each other. Imagine it as a waiter in a restaurant: you (the customer) tell the waiter what you want (a dish), and the waiter (the API)
#  relays your request to the chef (the software) and brings you back your order (the result).\n\n**API Potential: Unlocking the Full Scope**\n\nAn API's \"full potential\" refers to its ability to do far more than just pass data between applications. It's about creating a platform for innovation, connecting various services, and unlocking exciting possibilities. \n\nHere's a breakdown of how APIs unleash their full potential:\n\n*
#  **Connecting disparate systems:** APIs bridge the gap between different software and platforms, allowing them to share information and work together seamlessly.\n* **Building innovative services:** Developers can leverage APIs to create entirely new services, applications, and experiences that integrate data and functionalities from different sources.\n* **Automating workflows:** APIs automate repetitive tasks and processes, freeing up resources for more complex activities. \n* **Increasing efficiency and productivity:** APIs simplify the development process and enable quicker time-to-market for applications and services.\n* **Expanding the reach and scope:** APIs can extend the reach of businesses and their products/services by enabling them to connect with a wider user base and audience.\n* **Boosting data accessibility:** APIs offer a way to access and utilize data from various sources, empowering developers to build applications that rely on a wealth of information.\n* **Creating an ecosystem:** APIs enable the creation of a thriving ecosystem of interconnected services and applications, fostering collaboration and innovation.\n\n**Examples of API Full Potential in Action:**\n\n* **Weather apps:** API integration with meteorological data allows for highly accurate and dynamic weather forecasts.\n* **E-commerce:** APIs connect various platforms, enabling seamless purchase transactions between websites, payment processors, and delivery services.\n* **Social media:** API access allows developers to build applications that interact with social media platforms, enabling functionality like automated posting, hashtag analysis, and audience engagement.\n* **Mapping services:** API integration with map databases enables interactive maps, real-time traffic updates, and location-based services.\n\n**Exploring APIs**\n\nIf you're interested in learning more about APIs, here are some steps:\n\n* **Identify your needs:** What type of services do you want to build? \n* **Research APIs:** Use online resources like [https://www.rapidapi.com/](https://www.rapidapi.com/) and [https://www.apidocs.com/](https://www.apidocs.com/) to find APIs that match your requirements.\n* **Learn the basics:** Familiarize yourself with concepts like HTTP requests and API documentation.\n* **Start building:** Practice building small applications using APIs. Experiment and explore!\n\nThe full potential of APIs is immense. As technology advances, the use of APIs will continue to revolutionize how we interact with the digital world, and unlocking this potential will be key to the future of software and innovation. 
# \n\n\n\nLet me know if you want to dive deeper into any of these aspects or have specific API-related questions. \n"
# }