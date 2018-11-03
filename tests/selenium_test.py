
def test_home(selenium):
    selenium.get("http://162.246.156.154:8000")
    items = ["name", "about", "education", "skills", "work", "contact"]
    for item in items:
        res = selenium.find_element_by_id(item)
        print(res)
        assert res is not None