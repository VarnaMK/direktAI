from app.services.test_creation_service import (
    TestCreationService
)

service = TestCreationService()

result = service.create_test(
    requirement="Verify flight status for today's COK-SIN flight",
    application_url="https://example.com"
)

print("\n=== REQUIREMENT ANALYSIS ===")
print(
    result["requirement_analysis"]
)

print("\n=== APPLICATION DISCOVERY ===")
print(
    result["application_discovery"]
)

print("\n=== STEP GENERATION ===")
print(
    result["step_generation"]
)