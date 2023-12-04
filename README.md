# Tutorial for Python package calling a custom PyTorch C++ module

This is a minimal example of a Python package calling a custom PyTorch C++ module.

## Installing & running

1. Install requirements:
    ```bash
    pip install -r requirements.txt
    ```

2. Install package using `setup.py`:
    ```bash
    pip install -e .
    ```

3. Run the test:
    ```bash
    python main.py
    ```
    Expected result:
    ```
    tensor([5., 7., 9.])
    ```