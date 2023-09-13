# Python Stat Test Suite

This is a test suite for the exercises found in the "Python Statistiques.pdf" document.

## Prerequisites

Before running the test suite, you need to install NumPy. You can do this in one of the following ways:

### Option 1: Using pip (if your environment is not externally managed)

```bash
pip install numpy
```

### Option 2: Creating a virtual environment (if your environment is externally managed)

If your environment is externally managed, you can create a virtual environment and then install NumPy within it. Here are the steps:

1. Install the python3-venv package (if not already installed):

   ```bash
   sudo apt install python3-venv
   ```

2. Create a virtual environment (replace "myenv" with your preferred environment name):

   ```bash
   python3 -m venv myenv
   ```

3. Activate the virtual environment:

   ```bash
   source myenv/bin/activate
   ```

4. Install NumPy within the virtual environment:

   ```bash
   pip install numpy
   ```

### Option 3: Using pipx

Alternatively, you can use pipx to install NumPy:

1. Install pipx (if not already installed):

   ```bash
   sudo apt install pipx
   ```

2. Install NumPy using pipx:

   ```bash
   pipx install numpy
   ```

## Running the Test Suite

Once NumPy is installed, you can run the test suite with the following command :
  ```bash
  python3 test_suite_my_stat.py
  ```

