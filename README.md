# Thesis: Implementing a Quantum Arithmetic Logic Unit using the Qiskit SDK

## Quickstart
To start commiting changes to the repository, you may have to follow the steps below.
- Init a Python virtual enviroment.
```
python3 -m venv .venv
```
- Download, using PIP, the project's dependencies. The dependencies are noted in the file `requirements.txt`.
```
python3 -m pip install -r requirements.txt
```
- The project's is implemented using Jupyter Notebooks for Visual Studio Code. You can download the extension, for free, from [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter). You can, however, use Jupyter Lab to work but it's recommended to use VSCode (and all its derivatives).

## LaTeX dependencies
To display in LaTeX the circuit diagrams, you may need to install LaTeX for your system.
On Debian-based distributions, download using `apt`:
```
sudo apt install texlive texlive-latex-base texlive-latex-extra texlive-latex-recommended
```
On Arch-based Linux distributions, download using `pacman`:
```
sudo pacman -S texlive
```