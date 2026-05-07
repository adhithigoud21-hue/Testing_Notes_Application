#this file has the mcp testcases
from mcp.mcp_helper import MCPHelper


#This method will gebnerate the test data

def test_generate_test_data():

    data = MCPHelper.generate_test_data()

    print("\nGenerated Test Data:", data)

    assert "email" in data

    assert "password" in data

    assert data["email"] == "testuser@gmail.com"


# This method will anylze the failures

def test_failure_analysis():

    MCPHelper.analyze_failure(
        "Element not found"
    )

    assert True


#This method will suggest the locator

def test_locator_suggestion():

    MCPHelper.suggest_locator()

    assert True