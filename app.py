"""Module to access the Python assessment."""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/live-code-challenges")
def live_code_challenges():
    """The live-code-challenges page view."""

    return render_template("live-code-challenges.html", title="Live Code Challenges")


@app.route("/functions")
def functions():
    """The functions page view."""

    return render_template("functions.html", title="Functions")


@app.route("/data-types")
def data_types():
    """The data-types page view."""

    return render_template("data-types.html", title="Data Types")


@app.route("/data-structures")
def data_structures():
    """The data-structures page view."""

    return render_template("data-structures.html", title="Data Structures")


@app.route("/control-flow-logic")
def control_flow_logic():
    """The control-flow-logic page view."""

    return render_template("control-flow-logic.html", title="Control Flow Logic")


@app.route("/builtin-functions")
def builtin_functions():
    """The builtin-functions page view."""

    return render_template("builtin-functions.html", title="Builtin Functions")


@app.route("/")
@app.route("/assessment")
def assessment():
    """The assessment page view."""

    return render_template("assessment.html", title="Python Assessment")


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
