class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(list)
        email_to_name = {}

        for account in accounts:
            name = account[0]
            first_email = account[1]

            for email in account[1:]:
                email_to_name[email] = name

                graph[first_email].append(email)
                graph[email].append(first_email)
        
        visited = set()
        res = []

        for email in email_to_name:
            if email in visited:
                continue
            
            q = deque([email])
            visited.add(email)

            merged_emails = []

            while q:
                curr = q.popleft()
                merged_emails.append(curr)

                for nei in graph[curr]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
                
            merged_emails.sort()

            res.append(
                [email_to_name[email]] + merged_emails
            )

        return res