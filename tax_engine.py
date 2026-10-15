# ============================================================
# TAXWISE - TAX CALCULATION ENGINE
# Assessment Year: 2026-27
# ============================================================

AY = "2026-27"


# ============================================================
# HELPER FUNCTION
# ============================================================

def money(value):
    """Round a value to 2 decimal places."""
    return round(float(value), 2)


# ============================================================
# STANDARD DEDUCTION
# ============================================================

def get_standard_deduction(salary, regime):
    """
    Standard deduction for salaried income.

    New Regime : ₹75,000 maximum
    Old Regime : ₹50,000 maximum
    """

    if salary <= 0:
        return 0

    if regime == "new":
        return min(salary, 75000)

    return min(salary, 50000)


# ============================================================
# NEW TAX REGIME - TAX SLABS
# ============================================================

def calculate_new_regime_tax(taxable_income):
    """
    Calculate tax according to AY 2026-27
    New Tax Regime slabs.
    """

    tax = 0
    breakdown = []

    # --------------------------------------------------------
    # Up to ₹4,00,000
    # --------------------------------------------------------

    breakdown.append({
        "slab": "Up to ₹4,00,000",
        "rate": "0%",
        "amount": min(taxable_income, 400000),
        "tax": 0
    })

    # --------------------------------------------------------
    # ₹4,00,001 - ₹8,00,000
    # 5%
    # --------------------------------------------------------

    if taxable_income > 400000:

        amount = min(
            taxable_income,
            800000
        ) - 400000

        slab_tax = amount * 0.05

        tax += slab_tax

        breakdown.append({
            "slab": "₹4,00,001 – ₹8,00,000",
            "rate": "5%",
            "amount": amount,
            "tax": slab_tax
        })

    # --------------------------------------------------------
    # ₹8,00,001 - ₹12,00,000
    # 10%
    # --------------------------------------------------------

    if taxable_income > 800000:

        amount = min(
            taxable_income,
            1200000
        ) - 800000

        slab_tax = amount * 0.10

        tax += slab_tax

        breakdown.append({
            "slab": "₹8,00,001 – ₹12,00,000",
            "rate": "10%",
            "amount": amount,
            "tax": slab_tax
        })

    # --------------------------------------------------------
    # ₹12,00,001 - ₹16,00,000
    # 15%
    # --------------------------------------------------------

    if taxable_income > 1200000:

        amount = min(
            taxable_income,
            1600000
        ) - 1200000

        slab_tax = amount * 0.15

        tax += slab_tax

        breakdown.append({
            "slab": "₹12,00,001 – ₹16,00,000",
            "rate": "15%",
            "amount": amount,
            "tax": slab_tax
        })

    # --------------------------------------------------------
    # ₹16,00,001 - ₹20,00,000
    # 20%
    # --------------------------------------------------------

    if taxable_income > 1600000:

        amount = min(
            taxable_income,
            2000000
        ) - 1600000

        slab_tax = amount * 0.20

        tax += slab_tax

        breakdown.append({
            "slab": "₹16,00,001 – ₹20,00,000",
            "rate": "20%",
            "amount": amount,
            "tax": slab_tax
        })

    # --------------------------------------------------------
    # ₹20,00,001 - ₹24,00,000
    # 25%
    # --------------------------------------------------------

    if taxable_income > 2000000:

        amount = min(
            taxable_income,
            2400000
        ) - 2000000

        slab_tax = amount * 0.25

        tax += slab_tax

        breakdown.append({
            "slab": "₹20,00,001 – ₹24,00,000",
            "rate": "25%",
            "amount": amount,
            "tax": slab_tax
        })

    # --------------------------------------------------------
    # Above ₹24,00,000
    # 30%
    # --------------------------------------------------------

    if taxable_income > 2400000:

        amount = taxable_income - 2400000

        slab_tax = amount * 0.30

        tax += slab_tax

        breakdown.append({
            "slab": "Above ₹24,00,000",
            "rate": "30%",
            "amount": amount,
            "tax": slab_tax
        })

    return money(tax), breakdown


# ============================================================
# OLD TAX REGIME - TAX SLABS
# ============================================================

def calculate_old_regime_tax(taxable_income, age):
    """
    Calculate tax under the Old Tax Regime.

    Age below 60:
        Up to ₹2.5L       - Nil
        ₹2.5L - ₹5L       - 5%
        ₹5L - ₹10L        - 20%
        Above ₹10L        - 30%

    Age 60-79:
        Up to ₹3L         - Nil
        ₹3L - ₹5L         - 5%
        ₹5L - ₹10L        - 20%
        Above ₹10L        - 30%

    Age 80+:
        Up to ₹5L         - Nil
        ₹5L - ₹10L        - 20%
        Above ₹10L        - 30%
    """

    tax = 0
    breakdown = []

    # ========================================================
    # SUPER SENIOR CITIZEN - AGE 80+
    # ========================================================

    if age >= 80:

        breakdown.append({
            "slab": "Up to ₹5,00,000",
            "rate": "0%",
            "amount": min(taxable_income, 500000),
            "tax": 0
        })

        # ₹5L - ₹10L
        if taxable_income > 500000:

            amount = min(
                taxable_income,
                1000000
            ) - 500000

            slab_tax = amount * 0.20

            tax += slab_tax

            breakdown.append({
                "slab": "₹5,00,001 – ₹10,00,000",
                "rate": "20%",
                "amount": amount,
                "tax": slab_tax
            })

        # Above ₹10L
        if taxable_income > 1000000:

            amount = taxable_income - 1000000

            slab_tax = amount * 0.30

            tax += slab_tax

            breakdown.append({
                "slab": "Above ₹10,00,000",
                "rate": "30%",
                "amount": amount,
                "tax": slab_tax
            })

    # ========================================================
    # SENIOR CITIZEN - AGE 60 TO 79
    # ========================================================

    elif age >= 60:

        breakdown.append({
            "slab": "Up to ₹3,00,000",
            "rate": "0%",
            "amount": min(taxable_income, 300000),
            "tax": 0
        })

        # ₹3L - ₹5L
        if taxable_income > 300000:

            amount = min(
                taxable_income,
                500000
            ) - 300000

            slab_tax = amount * 0.05

            tax += slab_tax

            breakdown.append({
                "slab": "₹3,00,001 – ₹5,00,000",
                "rate": "5%",
                "amount": amount,
                "tax": slab_tax
            })

        # ₹5L - ₹10L
        if taxable_income > 500000:

            amount = min(
                taxable_income,
                1000000
            ) - 500000

            slab_tax = amount * 0.20

            tax += slab_tax

            breakdown.append({
                "slab": "₹5,00,001 – ₹10,00,000",
                "rate": "20%",
                "amount": amount,
                "tax": slab_tax
            })

        # Above ₹10L
        if taxable_income > 1000000:

            amount = taxable_income - 1000000

            slab_tax = amount * 0.30

            tax += slab_tax

            breakdown.append({
                "slab": "Above ₹10,00,000",
                "rate": "30%",
                "amount": amount,
                "tax": slab_tax
            })

    # ========================================================
    # NORMAL INDIVIDUAL - BELOW 60
    # ========================================================

    else:

        breakdown.append({
            "slab": "Up to ₹2,50,000",
            "rate": "0%",
            "amount": min(taxable_income, 250000),
            "tax": 0
        })

        # ₹2.5L - ₹5L
        if taxable_income > 250000:

            amount = min(
                taxable_income,
                500000
            ) - 250000

            slab_tax = amount * 0.05

            tax += slab_tax

            breakdown.append({
                "slab": "₹2,50,001 – ₹5,00,000",
                "rate": "5%",
                "amount": amount,
                "tax": slab_tax
            })

        # ₹5L - ₹10L
        if taxable_income > 500000:

            amount = min(
                taxable_income,
                1000000
            ) - 500000

            slab_tax = amount * 0.20

            tax += slab_tax

            breakdown.append({
                "slab": "₹5,00,001 – ₹10,00,000",
                "rate": "20%",
                "amount": amount,
                "tax": slab_tax
            })

        # Above ₹10L
        if taxable_income > 1000000:

            amount = taxable_income - 1000000

            slab_tax = amount * 0.30

            tax += slab_tax

            breakdown.append({
                "slab": "Above ₹10,00,000",
                "rate": "30%",
                "amount": amount,
                "tax": slab_tax
            })

    return money(tax), breakdown


# ============================================================
# NEW REGIME ₹12 LAKH MARGINAL RELIEF
# ============================================================

def calculate_new_regime_marginal_relief(
    taxable_income,
    tax_before_rebate,
    resident
):
    """
    Marginal relief for resident individuals under
    the New Tax Regime when taxable income is slightly
    above ₹12,00,000.

    Example:

    Income = ₹12,50,000
    Normal slab tax = ₹67,500

    Income above ₹12L = ₹50,000

    Therefore tax after marginal relief = ₹50,000
    """

    if not resident:
        return 0

    # Marginal relief applies only above ₹12L.
    if taxable_income <= 1200000:
        return 0

    # Marginal relief applies only while the
    # normal tax is greater than the excess income.
    excess_income = taxable_income - 1200000

    if tax_before_rebate <= excess_income:
        return 0

    relief = tax_before_rebate - excess_income

    return money(relief)


# ============================================================
# SURCHARGE RATE
# ============================================================

def get_surcharge_rate(total_income, regime):
    """
    Surcharge rates for AY 2026-27.

    New Regime:
        Up to ₹50L       = 0%
        ₹50L - ₹1Cr      = 10%
        ₹1Cr - ₹2Cr      = 15%
        ₹2Cr and above   = 25%

    Old Regime:
        Up to ₹50L       = 0%
        ₹50L - ₹1Cr      = 10%
        ₹1Cr - ₹2Cr      = 15%
        ₹2Cr - ₹5Cr      = 25%
        Above ₹5Cr       = 37%
    """

    if total_income <= 5000000:
        return 0

    if total_income <= 10000000:
        return 0.10

    if total_income <= 20000000:
        return 0.15

    if regime == "new":
        return 0.25

    if total_income <= 50000000:
        return 0.25

    return 0.37


# ============================================================
# TAX AT SURCHARGE THRESHOLD
# ============================================================

def calculate_tax_at_threshold(
    threshold,
    regime,
    age
):
    """
    Calculate base income tax at a surcharge threshold.
    Used for surcharge marginal relief.
    """

    if regime == "new":

        tax, _ = calculate_new_regime_tax(
            threshold
        )

        return tax

    tax, _ = calculate_old_regime_tax(
        threshold,
        age
    )

    return tax


# ============================================================
# SURCHARGE + SURCHARGE MARGINAL RELIEF
# ============================================================

def calculate_surcharge(
    tax_after_rebate,
    taxable_income,
    regime,
    age
):
    """
    Calculate surcharge and marginal relief from surcharge.
    """

    surcharge_rate = get_surcharge_rate(
        taxable_income,
        regime
    )

    if surcharge_rate == 0:

        return 0, 0

    surcharge_before_relief = (
        tax_after_rebate
        * surcharge_rate
    )

    # --------------------------------------------------------
    # Determine applicable threshold
    # --------------------------------------------------------

    if taxable_income > 50000000:

        threshold = 50000000

    elif taxable_income > 20000000:

        threshold = 20000000

    elif taxable_income > 10000000:

        threshold = 10000000

    else:

        threshold = 5000000

    # --------------------------------------------------------
    # Tax payable at threshold
    # --------------------------------------------------------

    threshold_tax = calculate_tax_at_threshold(
        threshold,
        regime,
        age
    )

    # --------------------------------------------------------
    # Maximum tax + surcharge allowed under
    # marginal relief
    # --------------------------------------------------------

    maximum_tax_with_relief = (
        threshold_tax
        + (taxable_income - threshold)
    )

    tax_plus_surcharge = (
        tax_after_rebate
        + surcharge_before_relief
    )

    # --------------------------------------------------------
    # Apply surcharge marginal relief
    # --------------------------------------------------------

    if tax_plus_surcharge > maximum_tax_with_relief:

        allowed_surcharge = max(
            0,
            maximum_tax_with_relief
            - tax_after_rebate
        )

        marginal_relief = (
            surcharge_before_relief
            - allowed_surcharge
        )

        return (
            money(allowed_surcharge),
            money(marginal_relief)
        )

    return (
        money(surcharge_before_relief),
        0
    )


# ============================================================
# MAIN TAX CALCULATOR
# ============================================================

def calculate_tax(
    salary,
    other_income,
    age,
    regime,
    deduction_80c=0,
    deduction_80d=0,
    resident=True
):
    """
    Main TaxWise calculation function.

    Parameters:
        salary
        other_income
        age
        regime
        deduction_80c
        deduction_80d
        resident

    Returns:
        Dictionary containing complete tax calculation.
    """

    # --------------------------------------------------------
    # Clean input values
    # --------------------------------------------------------

    salary = max(0, float(salary))
    other_income = max(0, float(other_income))

    deduction_80c = max(
        0,
        float(deduction_80c)
    )

    deduction_80d = max(
        0,
        float(deduction_80d)
    )

    age = int(age)

    if regime not in ["new", "old"]:
        regime = "new"

    # --------------------------------------------------------
    # Gross income
    # --------------------------------------------------------

    gross_income = (
        salary
        + other_income
    )

    # --------------------------------------------------------
    # Standard deduction
    # --------------------------------------------------------

    standard_deduction = get_standard_deduction(
        salary,
        regime
    )

    # --------------------------------------------------------
    # Old regime deductions
    # --------------------------------------------------------

    if regime == "old":

        # Section 80C maximum = ₹1,50,000
        allowed_80c = min(
            deduction_80c,
            150000
        )

        # TaxWise currently uses a simplified
        # 80D input.
        allowed_80d = min(
            deduction_80d,
            100000
        )

    else:

        # These deductions are not applied
        # in this TaxWise new-regime calculator.
        allowed_80c = 0
        allowed_80d = 0

    # --------------------------------------------------------
    # Total deductions
    # --------------------------------------------------------

    total_deductions = (
        standard_deduction
        + allowed_80c
        + allowed_80d
    )

    # --------------------------------------------------------
    # Taxable income
    # --------------------------------------------------------

    taxable_income = max(
        0,
        gross_income
        - total_deductions
    )

    # --------------------------------------------------------
    # Calculate slab tax
    # --------------------------------------------------------

    if regime == "new":

        tax_before_rebate, breakdown = (
            calculate_new_regime_tax(
                taxable_income
            )
        )

        regime_name = "New Tax Regime"

    else:

        tax_before_rebate, breakdown = (
            calculate_old_regime_tax(
                taxable_income,
                age
            )
        )

        regime_name = "Old Tax Regime"

    # --------------------------------------------------------
    # Section 87A rebate
    # --------------------------------------------------------

    rebate = 0

    if resident:

        # New regime
        if regime == "new":

            if taxable_income <= 1200000:

                rebate = min(
                    tax_before_rebate,
                    60000
                )

        # Old regime
        else:

            if taxable_income <= 500000:

                rebate = min(
                    tax_before_rebate,
                    12500
                )

    # --------------------------------------------------------
    # New regime marginal relief
    # --------------------------------------------------------

    marginal_relief_87a = 0

    if regime == "new":

        marginal_relief_87a = (
            calculate_new_regime_marginal_relief(
                taxable_income,
                tax_before_rebate,
                resident
            )
        )

    # --------------------------------------------------------
    # Tax after rebate / marginal relief
    # --------------------------------------------------------

    tax_after_rebate = max(
        0,
        tax_before_rebate
        - rebate
        - marginal_relief_87a
    )

    # --------------------------------------------------------
    # Surcharge
    # --------------------------------------------------------

    surcharge, surcharge_marginal_relief = (
        calculate_surcharge(
            tax_after_rebate,
            taxable_income,
            regime,
            age
        )
    )

    # --------------------------------------------------------
    # Health & Education Cess
    # --------------------------------------------------------

    cess = (
        tax_after_rebate
        + surcharge
    ) * 0.04

    # --------------------------------------------------------
    # Final tax
    # --------------------------------------------------------

    final_tax = (
        tax_after_rebate
        + surcharge
        + cess
    )

    # --------------------------------------------------------
    # Return complete result
    # --------------------------------------------------------

    return {

        # Basic information
        "assessment_year": AY,
        "regime": regime_name,
        "age": age,
        "resident": resident,

        # Income
        "salary": money(salary),
        "other_income": money(other_income),
        "gross_income": money(gross_income),

        # Deductions
        "standard_deduction": money(
            standard_deduction
        ),

        "deduction_80c": money(
            allowed_80c
        ),

        "deduction_80d": money(
            allowed_80d
        ),

        "total_deductions": money(
            total_deductions
        ),

        # Taxable income
        "taxable_income": money(
            taxable_income
        ),

        # Tax calculation
        "tax": money(
            tax_before_rebate
        ),

        "rebate": money(
            rebate
        ),

        "marginal_relief_87a": money(
            marginal_relief_87a
        ),

        "tax_after_rebate": money(
            tax_after_rebate
        ),

        # Surcharge
        "surcharge": money(
            surcharge
        ),

        "surcharge_marginal_relief": money(
            surcharge_marginal_relief
        ),

        # Cess
        "cess": money(
            cess
        ),

        # Final result
        "final_tax": money(
            final_tax
        ),

        # Slab details
        "breakdown": breakdown
    }
