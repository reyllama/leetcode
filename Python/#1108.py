"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".
"""

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')

"""
Runtime: 28 ms, faster than 81.15% of Python3 online submissions for Defanging an IP Address.
Memory Usage: 14.3 MB, less than 36.58% of Python3 online submissions for Defanging an IP Address.
"""
