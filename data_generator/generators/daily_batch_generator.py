from datetime import date, timedelta
from pathlib import Path
import random

import pandas as pd
from faker import Faker


fake = Faker()


# Project root:
# InsureFlow360/
PROJECT_ROOT = Path(__file__).resolve().parents[2]

OUTPUT_DIR = PROJECT_ROOT / "data_generator" / "output" / "csv"


def generate_policy_data(record_count: int = 100) -> pd.DataFrame:
    """Generate synthetic insurance policy data."""

    policy_types = [
        "Property",
        "Marine",
        "Casualty",
        "Professional Liability",
        "Cyber",
        "Motor",
    ]

    currencies = ["USD", "GBP", "EUR", "INR", "CAD", "AUD"]

    statuses = [
        "Active",
        "Pending",
        "Cancelled",
        "Expired",
    ]

    records = []

    batch_date = date.today()

    for i in range(1, record_count + 1):

        effective_date = batch_date - timedelta(
            days=random.randint(0, 365)
        )

        expiry_date = effective_date + timedelta(days=365)

        record = {
            "policy_id": f"POL{batch_date.strftime('%Y%m%d')}{i:05d}",
            "submission_id": f"SUB{random.randint(10000, 99999)}",
            "broker_id": f"BR{random.randint(1, 50):04d}",
            "insured_name": fake.company(),
            "policy_type": random.choice(policy_types),
            "effective_date": effective_date,
            "expiry_date": expiry_date,
            "premium": round(random.uniform(5000, 500000), 2),
            "currency": random.choice(currencies),
            "status": random.choice(statuses),
            "source_file_date": batch_date,
        }

        records.append(record)

    return pd.DataFrame(records)


def main() -> None:
    """Generate today's policy batch."""

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    batch_date = date.today()

    file_name = (
        f"policy_{batch_date.strftime('%Y%m%d')}.csv"
    )

    output_file = OUTPUT_DIR / file_name

    df = generate_policy_data(record_count=100)

    df.to_csv(
        output_file,
        index=False,
    )

    print(f"Generated {len(df)} policy records.")
    print(f"File: {output_file}")


if __name__ == "__main__":
    main()