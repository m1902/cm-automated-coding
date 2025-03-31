# Coaching Moves – Automated Coding

This guide explains how to set up an Ollama server on Oscar and run a Python project using it.

---

## 🖥️ Setting Up a Node and Ollama Server on Oscar

### Step 1: Log into Oscar

Use **PuTTY** (or another SSH client) to [connect to Oscar](https://docs.ccv.brown.edu/oscar/connecting-to-oscar/ssh):

```bash
ssh your_username@oscar_address
```

---

### Step 2: Add Ollama Models Path to Your Bash Profile

Run the following commands to make the Ollama models available:

```bash
echo 'export OLLAMA_MODELS=/oscar/data/shared/ollama_models' >> ~/.bashrc
source ~/.bashrc
```

This only needs to be done once. To verify if the variable contains a path to models, you may execute

```shell
echo $OLLAMA_MODELS
```

---

### Step 3: Start a GPU Node

Use `interact` to start a GPU node. For small models, 1 GPU is sufficient. For large models (e.g., Llama 70B), request 2 nodes.

Use `-t` option to adjust the time (10 minutes in the example below).

```bash
interact -n 4 -m 32g -q gpu -g 1 -t 0:10:00
```

Once the node is allocated, its name will be displayed 
(like `gpu2009`) and your prompt will change to something like:

```bash
[username@gpu2009 ~]$
```

If you're not automatically logged in, proceed to the next step.

---

### Step 4: Log into the Node (if needed)

Replace `gpu2009` with the actual name of your node:

```bash
ssh gpu2009
```

To leave the node, type:

```bash
exit
```

---

### Step 5: Start the Ollama Server

Load the module and start the Ollama server **inside your node**:

```bash
module load ollama
ollama serve &
```

When the server is ready (after several seconds), you’ll see something like this in the output:

```
Listening on 127.0.0.1:11434 (version 0.5.12)
looking for compatible GPUs
name="Quadro RTX 6000" total="23.6 GiB" available="23.5 GiB"
```

If a user prompt doesn't show in console, don't worry - you may continue working.

---

### Step 6: Use Ollama

- List available models:
  ```bash
  ollama list
  ```

- Run a specific model:
  ```bash
  ollama run llama3.1:8b
  ```

> ⚠️ If you're using the Python script, **do not** run models manually — the script will handle this.

---

## 🐍 Setting Up the Python Project

### Step 1: Create the `projects` Directory

You may execute this in a node, too (or directly after logging into Oscar):

```bash
mkdir -p ~/projects # creates a directory in your home directory
```

---

### Step 2: Clone the Git Repository

This is a one-time set-up of the repository:

```bash
cd ~/projects # move to projects directory
git clone https://github.com/m1902/cm-automated-coding
cd cm-automated-coding
```

---

### Step 3: Set Up the Python Environment

Create and activate a virtual environment (inside the `cm-automated-coding` directory):

```bash
cd cm-automated-coding # if you're not yet there
python -m venv venv
source venv/bin/activate
pip install ollama
```

To later activate or deactivate:

```bash
source venv/bin/activate  # activate
deactivate                # deactivate
```

---

## 🚀 Using the Project

Pull the current version from the git repository:

```bash
cd projects/cm-automated-coding # move to the directory
git pull # pull the changes
```

Activate the environment:

```bash
source venv/bin/activate
```

Run the script:

```bash
python ollama-test.py
```

> Replace `ollama-test.py` with any script you want to run.
