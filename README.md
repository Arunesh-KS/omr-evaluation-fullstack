# omr-evaluation-fullstack
A computer-vision driven desktop application built with Python (OpenCV/Tkinter) and MySQL to automate OMR sheet processing and manage academic records.
## 📁 Codebase Architecture

* **`src/OMRMAIN.py`**: The core execution script handling OpenCV window initialization, mouse-callback corner registration, and coordinate transformation loops.
* **`src/login.py`**: The main application entry point and user dashboard, managing Tkinter interface state transitions and routing data to the MySQL backend.
* **`src/f2.py`**: The internal image processing engine containing core matrix utility operations, including multi-dimensional pixel array splitting (`vsplit`/`hsplit`) and bubble density threshold evaluation.

---

## 📄 Technical Documentation

For a detailed look at the interface workflows, database schemas, and step-by-step visual outputs of each execution module, please refer to the project documentation available in the root directory:

👉 **[View the Module Walkthrough & System Outputs](./omr_evaluation_project_documentation.pdf)**
