from flask import Flask, render_template, request

from tax_engine import calculate_tax


app = Flask(__name__)


# ============================================================
# HOME / TAX CALCULATOR
# ============================================================

@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    name = ""

    if request.method == "POST":

        name = request.form.get("name", "").strip()

        salary_text = request.form.get(
            "salary",
            ""
        )

        other_income_text = request.form.get(
            "other_income",
            "0"
        )

        age_text = request.form.get(
            "age",
            ""
        )

        regime = request.form.get(
            "regime",
            "new"
        )

        deduction_80c_text = request.form.get(
            "deduction_80c",
            "0"
        )

        deduction_80d_text = request.form.get(
            "deduction_80d",
            "0"
        )

        try:

            salary = float(salary_text)
            other_income = float(other_income_text or 0)
            age = int(age_text)

            deduction_80c = float(
                deduction_80c_text or 0
            )

            deduction_80d = float(
                deduction_80d_text or 0
            )

            # ------------------------------------------------
            # Validation
            # ------------------------------------------------

            if salary < 0:
                result = {
                    "error":
                    "Salary cannot be negative."
                }

            elif other_income < 0:
                result = {
                    "error":
                    "Other income cannot be negative."
                }

            elif age < 1 or age > 120:
                result = {
                    "error":
                    "Please enter a valid age."
                }

            elif deduction_80c < 0:
                result = {
                    "error":
                    "80C deduction cannot be negative."
                }

            elif deduction_80d < 0:
                result = {
                    "error":
                    "80D deduction cannot be negative."
                }

            else:

                result = calculate_tax(

                    salary=salary,

                    other_income=other_income,

                    age=age,

                    regime=regime,

                    deduction_80c=
                        deduction_80c,

                    deduction_80d=
                        deduction_80d
                )

        except ValueError:

            result = {
                "error":
                "Please enter valid numbers in all required fields."
            }

    return render_template(
        "index.html",
        result=result,
        name=name
    )


# ============================================================
# LEARN PAGE
# ============================================================

@app.route("/learn")
def learn():

    return render_template(
        "learn.html"
    )


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )
