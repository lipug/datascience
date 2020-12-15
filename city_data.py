city_revenues = pd.Series(
    [4200, 8000, 6500],
    index=["Amsterdam", "Toronto", "Tokyo"]
)

city_employee_count = pd.Series({"Amsterdam": 5, "Tokyo": 8})

city_data = pd.DataFrame({
    "revenue": city_revenues,
    "employee_count": city_employee_count
})