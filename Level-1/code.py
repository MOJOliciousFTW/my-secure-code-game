"""
////////////////////////////////////////////////////////////
///                                                      ///
///   0. tests.py is passing but the code is vulnerable  /// 
///   1. Review the code. Can you spot the bug?          ///
///   2. Fix the code but ensure that tests.py passes    ///
///   3. Run hack.py and if passing then CONGRATS!       ///
///   4. If stucked then read the hint                   ///
///   5. Compare your solution with solution.py          ///
///                                                      ///
////////////////////////////////////////////////////////////
"""

from dataclasses import dataclass


@dataclass
class Order:
    id: str
    items: list


@dataclass
class Item:
    type: str
    description: str
    amount: float
    quantity: int


def validorder(order: Order):
    net = 0  # net amount paid in cents

    for item in order.items:
        if item.type == "payment":
            net += int(100 * item.amount)
        elif item.type == "product":
            net -= int(100 * item.amount * item.quantity)
        else:
            return "Invalid item type: %s" % item.type

    if net != 0:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net / 100)
    else:
        return "Order ID: %s - Full payment received!" % order.id
