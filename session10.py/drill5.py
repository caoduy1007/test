listData = [
    {"name": "Huy",
    " role": "waiter",
    "hours": 12,
    "salary per hours($)": 0.8,
    },
    {"name": "Tung",
    " role": "Cook",
    "hours": 24,
    "salary per hours($)": 1.5,
    },
    {"name": "M.Duc",
    " role": "manager",
    "hours": 20,
    "salary per hours($)": 2,
    }
]
print(*listData)
newData = [
    {"name": "Don",
    " role": "waiter",
    "hours": 12,
    "salary per hours($)": 0.9,
    },
    {"name": "H.Duc",
    " role": "waiter",
    "hours": 14,
    "salary per hours($)": 0.7,
    }
]
listData.append(newData)
for x in listData:
    print(x)