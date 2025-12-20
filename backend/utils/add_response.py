import json
import os

def initialize_json():
    """Create empty responses.json if it doesn't exist"""
    data_dir = '../data'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    output_file = os.path.join(data_dir, 'responses.json')
    
    if not os.path.exists(output_file):
        initial_data = {"prompts": []}
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(initial_data, f, indent=2, ensure_ascii=False)
        print(f"✅ Created new responses.json")
    return output_file

def add_prompt_with_responses(prompt_text, responses_list):
    """
    Add a complete prompt with all model responses
    
    responses_list should be a list of dictionaries with:
    - model_name
    - model_type
    - provider
    - response (the actual text - paste it here, Python handles formatting!)
    - response_time
    - token_count
    - strengths (list)
    """
    output_file = initialize_json()
    
    # Load existing data
    with open(output_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Create new prompt entry
    new_id = len(data["prompts"]) + 1
    new_prompt = {
        "id": new_id,
        "prompt": prompt_text,
        "responses": responses_list
    }
    
    data["prompts"].append(new_prompt)
    
    # Save back
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Added prompt #{new_id}: '{prompt_text}'")
    print(f"   Added {len(responses_list)} model responses")

# ============================================
# ADD YOUR RESPONSES HERE
# ============================================

# Prompt 1: What is AI?
prompt1_responses = [
    {
        "model_name": "GPT-4",
        "model_type": "LLM",
        "provider": "OpenAI",
        "response": """AI (Artificial Intelligence) is a branch of computer science that focuses on creating machines or software that can **think, learn, and make decisions** similar to humans.

### **Simple Definition**

AI is when a computer or machine is designed to do tasks that normally need human intelligence—like learning, understanding, reasoning, or solving problems.

### **Examples in Daily Life**

* **Google Maps** finding the best route
* **ChatGPT** answering questions
* **Face unlock** on phones
* **Netflix/YouTube** recommending videos
* **Alexa/Siri** understanding voice commands

### **Types of AI**

1. **Narrow AI**

   * Designed for one specific task (e.g., chess-playing AI, recommendation systems).

2. **General AI**

   * A hypothetical AI that can think and learn like a human across all tasks (not yet achieved).

### **How AI Works (Basic Idea)**

AI uses:

* **Data** (examples to learn from)
* **Algorithms** (rules/models that learn patterns)
* **Computing power** (to train and run models)

For example, showing a computer thousands of cat images helps it *learn* what a cat looks like.

---

If you want, I can explain AI in even simpler words or relate it to your pre-placement talk for Fractal Analytics!

""",
        "response_time": 2.3,
        "token_count": 145,
        "strengths": ["detailed explanations", "context understanding"]
    },
    {
        "model_name": "Claude-3",
        "model_type": "LLM",
        "provider": "Anthropic",
        "response": """AI, or artificial intelligence, is technology that enables machines to perform tasks that typically require human intelligence. This includes things like understanding language, recognizing patterns, making decisions, and learning from experience.

There are different types of AI:

**Narrow AI** (what we have today) is designed for specific tasks - like recommending movies, translating languages, or playing chess. Most AI you interact with falls into this category, including me.

**General AI** (still theoretical) would match human-level intelligence across a wide range of tasks and contexts, with the ability to learn and adapt like humans do.

At its core, modern AI often works through machine learning, where systems learn patterns from large amounts of data rather than being explicitly programmed for every scenario. For example, I was trained on vast amounts of text to learn patterns in language, which allows me to understand and generate human-like responses.

AI is increasingly woven into everyday life - in voice assistants, recommendation algorithms, medical diagnostics, autonomous vehicles, and countless other applications. It's a rapidly evolving field that raises both exciting possibilities and important questions about ethics, employment, privacy, and how we want to shape our technological future.

Is there a particular aspect of AI you're curious about?""",
        "response_time": 1.8,
        "token_count": 138,
        "strengths": ["technical accuracy", "structured responses"]
    },
    {
        "model_name": "Gemini Pro",
        "model_type": "LLM",
        "provider": "Google",
        "response": """Machine Learning (ML) is a subset of Artificial Intelligence (AI) that allows computers to **learn from data** without being explicitly programmed.

Instead of a programmer writing specific rules for every possible scenario (e.g., "If the photo has an ear and whiskers, it's a cat"), the computer develops its **own set of rules** by analyzing thousands of examples.

## 🍎 The Simple Analogy: Teaching a Child

Imagine you are teaching a child (the machine) to recognize an apple.

1.  **Give it Data (The Training Set):** You show the child thousands of pictures of apples and other things (bananas, cars, flowers), and you **label** each one (e.g., "This is an apple," "This is NOT an apple").
2.  **The Algorithm Learns (The Model):** The child's brain (the ML algorithm) processes these examples and starts figuring out patterns: "Apples are usually round, red/green/yellow, and have a small stem." This set of learned patterns is called the **model**.
3.  **Make a Prediction (Inference):** You show the child a brand-new, unseen picture. Based on the patterns it learned, the child can confidently say, "That's an apple!" The more examples it sees, the better and more accurate its guesses become.

This is the core idea: **Learning from examples to make predictions or decisions on new data.** 

---

## 🏗️ The Three Main Types of Machine Learning

ML models are generally categorized by the way they are **trained** on the data:

### 1. Supervised Learning
* **The Teacher is Present:** The training data is **labeled** (has a "correct answer" or output).
* **Goal:** To learn the mapping between the input and the known output.
* **Examples:**
    * **Classification:** Predicting a **category** (e.g., Is this email **spam** or **not spam**?).
    * **Regression:** Predicting a **continuous value** (e.g., What will the price of this house be?).

### 2. Unsupervised Learning
* **No Teacher, Just Exploration:** The training data is **unlabeled** (no pre-defined outputs).
* **Goal:** The algorithm must find hidden structures, patterns, or groupings on its own.
* **Examples:**
    * **Clustering:** Grouping similar customers together for marketing (e.g., identifying groups of people who buy similar products).
    * **Dimensionality Reduction:** Simplifying complex data while keeping the most important information.

### 3. Reinforcement Learning (RL)
* **Learning by Trial and Error:** The algorithm (often called an "agent") learns by interacting with an environment. It receives **rewards** for good actions and **penalties** for bad ones.
* **Goal:** To maximize the cumulative reward over time.
* **Examples:**
    * Training a computer to **play chess or Go** (getting rewarded for winning).
    * Teaching a **robot** to navigate a room.

---

Machine learning is the fundamental technology behind many things you use every day, including Netflix recommendations, search engine results, and virtual assistants.

This video provides an intuitive breakdown of various machine learning algorithms, which are the "recipes" the models follow to learn from data: [All Machine Learning algorithms explained in 17 min](https://www.youtube.com/watch?v=E0Hmnixke2g).


http://googleusercontent.com/youtube_content/0
""",
        "response_time": 1.5,
        "token_count": 125,
        "strengths": ["speed", "conciseness"]
    },
    {
        "model_name": "Llama-3-70B",
        "model_type": "LLM",
        "provider": "Meta",
        "response": """AI stands for Artificial Intelligence. It's a field of computer science that focuses on creating intelligent machines that can think and learn like humans.

AI involves training computers to perform tasks that typically require human intelligence, such as:

- Learning: AI systems can learn from data, experiences, and interactions.
- Reasoning: AI can make decisions, solve problems, and draw conclusions.
- Perception: AI can interpret and understand visual, auditory, or sensory data.
- Language Understanding: AI can process, understand, and generate human language.

There are several types of AI, including:

- Narrow or Weak AI: Designed for specific tasks, like virtual assistants or image recognition.
- General or Strong AI: A hypothetical AI that can perform any intellectual task a human can.
- Superintelligence: A hypothetical AI that's significantly more intelligent than the best human minds.

AI has many applications, such as:

- Virtual Assistants: Like Siri, Alexa, or Google Assistant.
- Image Recognition: Used in self-driving cars, facial recognition, and medical diagnosis.
- Natural Language Processing: Used in chatbots, language translation, and sentiment analysis.
- Predictive Analytics: Used in finance, marketing, and healthcare to forecast outcomes.

That's a brief overview of AI!""",
        "response_time": 2.1,
        "token_count": 152,
        "strengths": ["open-source", "versatility"]
    },
    {
        "model_name": "Mistral-7B",
        "model_type": "SLM",
        "provider": "Mistral AI",
        "response": """**AI (Artificial Intelligence)** is the simulation of human intelligence in machines that are programmed to think, learn, and problem-solve like humans. It involves creating computer systems capable of performing tasks that typically require human intelligence, such as:

- **Understanding and generating language** (like me!)
- **Recognizing patterns** in data (images, speech, text)
- **Making decisions** based on information
- **Learning from experience** and improving over time

AI powers many technologies you use daily—from voice assistants and recommendation systems to self-driving cars and advanced medical diagnostics.

Would you like to know how AI works, its different types, or its real-world applications?""",
        "response_time": 1.2,
        "token_count": 118,
        "strengths": ["efficiency", "small model size"]
    },
    {
        "model_name": "Phi-3",
        "model_type": "SLM",
        "provider": "Microsoft",
        "response": """Paste your Phi-3 response here.""",
        "response_time": 1.0,
        "token_count": 105,
        "strengths": ["compact", "fast inference"]
    }
]

# Prompt 2: Explain machine learning in simple terms
prompt2_responses = [
    {
        "model_name": "GPT-4",
        "model_type": "LLM",
        "provider": "OpenAI",
        "response": """Machine Learning (ML) is a part of AI that teaches computers to **learn from examples instead of being directly programmed**.

### **Simple Definition**

Machine learning is when you give a computer lots of data, and it figures out patterns on its own so it can make decisions or predictions.

---

### **Super Simple Example**

If you want a computer to recognize cats:

* You **don’t** write rules like “cats have whiskers, fur, tail...”
* Instead, you **show the computer thousands of pictures** of cats and non-cats.
* The computer *learns* the patterns (shapes, colors, textures).
* Next time it sees a picture, it can guess: “This is a cat” or “Not a cat.”

---

### **Everyday Examples of Machine Learning**

* **YouTube/Netflix** suggesting videos
* **Spam filter** detecting unwanted emails
* **Amazon** recommending products
* **Google Photos** grouping similar faces
* **Instagram** showing you posts you may like

---

### **Why It’s Called “Learning”**

Because the computer improves over time as it sees more data—just like humans do.

---

If you want, I can also explain types of machine learning (like supervised, unsupervised, reinforcement) in the same simple way.
""",
        "response_time": 2.5,
        "token_count": 180,
        "strengths": ["detailed explanations", "context understanding"]
    },
    {
        "model_name": "Claude-3",
        "model_type": "LLM",
        "provider": "Anthropic",
        "response": """Machine learning is essentially teaching computers to learn from examples rather than giving them step-by-step instructions.

Think of it like teaching a child to recognize dogs. You don't give them a rulebook saying "if it has four legs AND fur AND barks, then it's a dog." Instead, you show them many pictures of dogs - big ones, small ones, different breeds - and eventually they figure out the pattern themselves. Machine learning works similarly.

**Here's the basic process:**

The computer is fed lots of examples (data) - like thousands of photos labeled "dog" or "cat." It looks for patterns in that data, makes guesses, checks if those guesses are right or wrong, and adjusts its approach. Over time, through trial and error, it gets better at making accurate predictions on new examples it hasn't seen before.

**A simple example:** Teaching a computer to recognize spam emails. You feed it thousands of emails labeled "spam" or "not spam." It notices patterns - maybe spam often contains certain words like "free money" or comes from suspicious addresses. After learning from these examples, it can look at a brand new email and predict whether it's likely spam.

The key difference from traditional programming is that you're not telling the computer the rules - you're letting it discover the rules by learning from data. This is powerful because it can find patterns that might be too complex or subtle for humans to explicitly program.""",
        "response_time": 2.0,
        "token_count": 175,
        "strengths": ["technical accuracy", "structured responses"]
    },
    {
        "model_name": "Gemini Pro",
        "model_type": "LLM",
        "provider": "Google",
        "response": """Machine Learning (ML) is a subset of Artificial Intelligence (AI) that allows computers to **learn from data** without being explicitly programmed.

Instead of a programmer writing specific rules for every possible scenario (e.g., "If the photo has an ear and whiskers, it's a cat"), the computer develops its **own set of rules** by analyzing thousands of examples.

## 🍎 The Simple Analogy: Teaching a Child

Imagine you are teaching a child (the machine) to recognize an apple.

1.  **Give it Data (The Training Set):** You show the child thousands of pictures of apples and other things (bananas, cars, flowers), and you **label** each one (e.g., "This is an apple," "This is NOT an apple").
2.  **The Algorithm Learns (The Model):** The child's brain (the ML algorithm) processes these examples and starts figuring out patterns: "Apples are usually round, red/green/yellow, and have a small stem." This set of learned patterns is called the **model**.
3.  **Make a Prediction (Inference):** You show the child a brand-new, unseen picture. Based on the patterns it learned, the child can confidently say, "That's an apple!" The more examples it sees, the better and more accurate its guesses become.

This is the core idea: **Learning from examples to make predictions or decisions on new data.** 

---

## 🏗️ The Three Main Types of Machine Learning

ML models are generally categorized by the way they are **trained** on the data:

### 1. Supervised Learning
* **The Teacher is Present:** The training data is **labeled** (has a "correct answer" or output).
* **Goal:** To learn the mapping between the input and the known output.
* **Examples:**
    * **Classification:** Predicting a **category** (e.g., Is this email **spam** or **not spam**?).
    * **Regression:** Predicting a **continuous value** (e.g., What will the price of this house be?).

### 2. Unsupervised Learning
* **No Teacher, Just Exploration:** The training data is **unlabeled** (no pre-defined outputs).
* **Goal:** The algorithm must find hidden structures, patterns, or groupings on its own.
* **Examples:**
    * **Clustering:** Grouping similar customers together for marketing (e.g., identifying groups of people who buy similar products).
    * **Dimensionality Reduction:** Simplifying complex data while keeping the most important information.

### 3. Reinforcement Learning (RL)
* **Learning by Trial and Error:** The algorithm (often called an "agent") learns by interacting with an environment. It receives **rewards** for good actions and **penalties** for bad ones.
* **Goal:** To maximize the cumulative reward over time.
* **Examples:**
    * Training a computer to **play chess or Go** (getting rewarded for winning).
    * Teaching a **robot** to navigate a room.

---

Machine learning is the fundamental technology behind many things you use every day, including Netflix recommendations, search engine results, and virtual assistants.

This video provides an intuitive breakdown of various machine learning algorithms, which are the "recipes" the models follow to learn from data: [All Machine Learning algorithms explained in 17 min](https://www.youtube.com/watch?v=E0Hmnixke2g).


http://googleusercontent.com/youtube_content/0
""",
        "response_time": 1.7,
        "token_count": 165,
        "strengths": ["speed", "conciseness"]
    },
    {
        "model_name": "Llama-3-70B",
        "model_type": "LLM",
        "provider": "Meta",
        "response": """Machine learning is like teaching a computer to learn from experience. You show it lots of examples, and it figures out patterns and rules on its own. Then, it can make predictions or decisions about new, unseen data.

Think of it like teaching a kid to recognize dogs:

1. You show them lots of pictures of dogs and say, "This is a dog."
2. They learn to recognize patterns like fur, four legs, and a tail.
3. Next time they see a new picture, they can say, "That's a dog!"

Machine learning is similar, but instead of pictures, computers learn from data. There are different types, like:

- Supervised learning (like the dog example)
- Unsupervised learning (finding patterns in data without labels)
- Reinforcement learning (learning through trial and error)

It's a powerful tool that enables computers to improve themselves and make predictions or decisions without being explicitly programmed.""",
        "response_time": 2.3,
        "token_count": 190,
        "strengths": ["open-source", "versatility"]
    },
    {
        "model_name": "Mistral-7B",
        "model_type": "SLM",
        "provider": "Mistral AI",
        "response": """**Machine Learning (ML)** is a type of AI that allows computers to learn from data, without being explicitly programmed for every single task.

### How it works (in simple terms):
Imagine you’re teaching a child to recognize cats. You show them lots of pictures of cats and say, “This is a cat.” After seeing enough examples, the child starts to recognize cats on their own, even in new pictures they’ve never seen before.

Machine learning works similarly:
- You feed a computer lots of data (like pictures, numbers, or text).
- The computer looks for patterns in that data.
- It uses those patterns to make predictions or decisions about new, unseen data.

### Example:
- **Email spam filter:** You mark emails as “spam” or “not spam.” The computer learns from your choices and starts filtering new emails automatically.

### Why it’s powerful:
Instead of writing thousands of rules (like “if the email has the word ‘free,’ mark as spam”), the computer learns the rules itself from examples.

Would you like a real-world analogy or an example of how ML is used in everyday life?""",
        "response_time": 1.4,
        "token_count": 155,
        "strengths": ["efficiency", "small model size"]
    },
    {
        "model_name": "Phi-3",
        "model_type": "SLM",
        "provider": "Microsoft",
        "response": """Paste Phi-3 response here.""",
        "response_time": 1.1,
        "token_count": 145,
        "strengths": ["compact", "fast inference"]
    }
]

# Prompt 3: Write a Python function to calculate factorial
prompt3_responses = [
    {
        "model_name": "GPT-4",
        "model_type": "LLM",
        "provider": "OpenAI",
        "response": """def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
""",
        "response_time": 1.8,
        "token_count": 120,
        "strengths": ["detailed explanations", "context understanding"]
    },
    {
        "model_name": "Claude-3",
        "model_type": "LLM",
        "provider": "Anthropic",
        "response": """def factorial(n):
    Calculate the factorial of n (n!)
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Example usage
print(factorial(5))   # Output: 120
print(factorial(0))   # Output: 1
print(factorial(10))  # Output: 3628800""",
        "response_time": 1.5,
        "token_count": 115,
        "strengths": ["technical accuracy", "structured responses"]
    },
    {
        "model_name": "Gemini Pro",
        "model_type": "LLM",
        "provider": "Google",
        "response": """def factorial_iterative(n):
    
    Calculates the factorial of a non-negative integer 'n' using an iterative approach.
    
    Args:
        n (int): The number for which to calculate the factorial.
        
    Returns:
        int: The factorial of n. Returns 1 for n=0.
        
    Raises:
        ValueError: If n is a negative number.
    
    # Handle negative input
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    # Factorial of 0 is 1
    if n == 0:
        return 1
    
    result = 1
    # Multiply result by every number from 1 up to n
    for i in range(1, n + 1):
        result *= i
        
    return result

# Example Usage
print(f"Factorial of 5 (iterative): {factorial_iterative(5)}")
print(f"Factorial of 0 (iterative): {factorial_iterative(0)}")""",
        "response_time": 1.3,
        "token_count": 110,
        "strengths": ["speed", "conciseness"]
    },
    {
        "model_name": "Llama-3-70B",
        "model_type": "LLM",
        "provider": "Meta",
        "response": """
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Example usage:
print(factorial(5))  # Output: 120


This function uses recursion to calculate the factorial of a given number n. If n is 0 or 1, it returns 1 (since 0! and 1! are both 1). Otherwise, it calls itself with n-1 until it reaches the base case.

Alternatively, you can use an iterative approach:


def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Example usage:
print(factorial(5))  # Output: 120


This function uses a loop to calculate the factorial of n.""",
        "response_time": 1.7,
        "token_count": 125,
        "strengths": ["open-source", "versatility"]
    },
    {
        "model_name": "Mistral-7B",
        "model_type": "SLM",
        "provider": "Mistral AI",
        "response": """def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
print(factorial(5))  # Output: 120
How it works:

The function calls itself (recursion) to multiply the number by the factorial of the number minus one.
The base case is when n is 0 or 1, in which case the factorial is 1.
Would you like an iterative version (using a loop) as well?
""",
        "response_time": 1.0,
        "token_count": 105,
        "strengths": ["efficiency", "small model size"]
    },
    {
        "model_name": "Phi-3",
        "model_type": "SLM",
        "provider": "Microsoft",
        "response": """Paste Phi-3 code here.""",
        "response_time": 0.8,
        "token_count": 100,
        "strengths": ["compact", "fast inference"]
    }
]

# Prompt 4: What are the benefits of renewable energy?
prompt4_responses = [
    {
        "model_name": "GPT-4",
        "model_type": "LLM",
        "provider": "OpenAI",
        "response": """Paste GPT-4 renewable energy response here.""",
        "response_time": 2.7,
        "token_count": 200,
        "strengths": ["detailed explanations", "context understanding"]
    },
    {
        "model_name": "Claude-3",
        "model_type": "LLM",
        "provider": "Anthropic",
        "response": """Paste Claude renewable energy response here.""",
        "response_time": 2.2,
        "token_count": 195,
        "strengths": ["technical accuracy", "structured responses"]
    },
    {
        "model_name": "Gemini Pro",
        "model_type": "LLM",
        "provider": "Google",
        "response": """Paste Gemini response here.""",
        "response_time": 1.9,
        "token_count": 185,
        "strengths": ["speed", "conciseness"]
    },
    {
        "model_name": "Llama-3-70B",
        "model_type": "LLM",
        "provider": "Meta",
        "response": """Paste Llama response here.""",
        "response_time": 2.5,
        "token_count": 210,
        "strengths": ["open-source", "versatility"]
    },
    {
        "model_name": "Mistral-7B",
        "model_type": "SLM",
        "provider": "Mistral AI",
        "response": """Paste Mistral response here.""",
        "response_time": 1.6,
        "token_count": 175,
        "strengths": ["efficiency", "small model size"]
    },
    {
        "model_name": "Phi-3",
        "model_type": "SLM",
        "provider": "Microsoft",
        "response": """Paste Phi-3 response here.""",
        "response_time": 1.3,
        "token_count": 165,
        "strengths": ["compact", "fast inference"]
    }
]

# Prompt 5: Explain quantum computing
prompt5_responses = [
    {
        "model_name": "GPT-4",
        "model_type": "LLM",
        "provider": "OpenAI",
        "response": """Paste GPT-4 quantum computing response here.""",
        "response_time": 3.0,
        "token_count": 220,
        "strengths": ["detailed explanations", "context understanding"]
    },
    {
        "model_name": "Claude-3",
        "model_type": "LLM",
        "provider": "Anthropic",
        "response": """Paste Claude quantum computing response here.""",
        "response_time": 2.5,
        "token_count": 215,
        "strengths": ["technical accuracy", "structured responses"]
    },
    {
        "model_name": "Gemini Pro",
        "model_type": "LLM",
        "provider": "Google",
        "response": """Paste Gemini response here.""",
        "response_time": 2.2,
        "token_count": 205,
        "strengths": ["speed", "conciseness"]
    },
    {
        "model_name": "Llama-3-70B",
        "model_type": "LLM",
        "provider": "Meta",
        "response": """Paste Llama response here.""",
        "response_time": 2.8,
        "token_count": 230,
        "strengths": ["open-source", "versatility"]
    },
    {
        "model_name": "Mistral-7B",
        "model_type": "SLM",
        "provider": "Mistral AI",
        "response": """Paste Mistral response here.""",
        "response_time": 1.9,
        "token_count": 195,
        "strengths": ["efficiency", "small model size"]
    },
    {
        "model_name": "Phi-3",
        "model_type": "SLM",
        "provider": "Microsoft",
        "response": """Paste Phi-3 response here.""",
        "response_time": 1.6,
        "token_count": 185,
        "strengths": ["compact", "fast inference"]
    }
]

# ============================================
# RUN THIS TO ADD ALL PROMPTS
# ============================================
if __name__ == "__main__":
    print("🚀 Starting to build responses.json...\n")
    
    # Delete old file if exists (fresh start)
    import os
    output_file = '../data/responses.json'
    if os.path.exists(output_file):
        os.remove(output_file)
        print("🗑️  Removed old responses.json\n")
    
    # Add all prompts
    add_prompt_with_responses("What is AI?", prompt1_responses)
    add_prompt_with_responses("Explain machine learning in simple terms", prompt2_responses)
    add_prompt_with_responses("Write a Python function to calculate factorial", prompt3_responses)
    add_prompt_with_responses("What are the benefits of renewable energy?", prompt4_responses)
    add_prompt_with_responses("Explain quantum computing", prompt5_responses)
    
    print("\n✅ Done! responses.json created successfully!")
    print("📁 Location: backend/data/responses.json")
    print("\n⚠️  Now replace the placeholder texts with actual AI responses")