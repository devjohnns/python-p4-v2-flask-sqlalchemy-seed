#!/usr/bin/env python3
# server/faker_demo.py

from faker import Faker

# Create and initialize a faker generator
fake = Faker()

print("Faker Demo - Generating Random Data")
print("=" * 40)

print("\nRandom names:")
for i in range(5):
    print(f"  {fake.name()}")

print("\nRandom first names:")
for i in range(5):
    print(f"  {fake.first_name()}")

print("\nRandom last names:")
for i in range(5):
    print(f"  {fake.last_name()}")

print("\nRandom emails:")
for i in range(3):
    print(f"  {fake.email()}")

print("\nRandom colors:")
for i in range(3):
    print(f"  {fake.color()}")

print("\nRandom addresses:")
for i in range(2):
    print(f"  {fake.address()}")