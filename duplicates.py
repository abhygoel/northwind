class DuplicateFinder:
    def __init__(self):
        self.repeated = {}
        self.first_seen = {}
        self.customer_by_email = {}
        self.customer_by_phone = {}
        self.total_rows = 0
        self.names = {}

    def add(self, cleaned):
        self.total_rows += 1
        customer_id = cleaned["customer_id"]
        row_key = (cleaned["name"], cleaned["email"], cleaned["phone"], cleaned["city"])
        if row_key in self.first_seen:
            self.repeated[customer_id] = self.first_seen[row_key]
        else:
            self.first_seen[row_key] = customer_id
            self.names[customer_id] = cleaned["name"]
            if cleaned["email"]:
                self.customer_by_email.setdefault(cleaned["email"], []).append(customer_id)
            if cleaned["phone"]:
                self.customer_by_phone.setdefault(cleaned["phone"], []).append(customer_id)

    def copies(self):
        return self.repeated

    def same_email_groups(self):
        email_group = {}
        for email, ids in self.customer_by_email.items():
            if len(ids) >= 2:
                email_group[email] = ids
        return dict(sorted(email_group.items(), key=lambda item: len(item[1]), reverse=True))

    def shared_phone_groups(self):
        phone_group = {}
        email_group_ids = set()
        for ids in self.same_email_groups().values():
            email_group_ids.update(ids)
        for phone, ids in self.customer_by_phone.items():
            unexplained = set(ids) - email_group_ids
            if len(ids) >= 2 and unexplained:
                phone_group[phone] = ids
        return dict(sorted(phone_group.items(), key=lambda item: len(item[1]), reverse=True))