
class PaginatedNewsIterator:
    def __init__(self, headlines, per_page=3):
        self.headlines = headlines
        self.per_page = per_page
        self.current_page = 0
        self.total_pages = (len(headlines) + per_page - 1) // per_page

    def get_page(self):
        start = self.current_page * self.per_page
        end = start + self.per_page
        return self.headlines[start:end]

    def next_page(self):
        if self.current_page < self.total_pages - 1:
            self.current_page += 1
        else:
            print(" You are on the last page.")

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
        else:
            print(" You are on the first page.")

    def display(self):
        page = self.get_page()
        print(f"\n Page {self.current_page + 1}/{self.total_pages}")
        print("-" * 40)
        for idx, headline in enumerate(page, start=1):
            print(f"{idx + self.current_page * self.per_page}. {headline}")
        print("-" * 40)


# ---  Usage ---
if __name__ == "__main__":
    headlines = [
        "AI breakthrough in cancer research",
        "Global markets hit new high",
        "NASA announces Moon mission crew",
        "Electric vehicles outsell gas cars",
        "Climate summit tackles global goals",
        "Tech giants face new regulations",
        "Breakthrough in quantum computing",
        "New planet discovered in solar system",
        "Major cities adopt smart traffic tech",
        "Education reforms announced"
    ]

    paginator = PaginatedNewsIterator(headlines)

    while True:
        paginator.display()
        command = input("Enter command (n = next, p = prev, q = quit): ").lower()

        if command == 'n':
            paginator.next_page()
        elif command == 'p':
            paginator.prev_page()
        elif command == 'q':
            print(" Exiting pagination.")
            break
        else:
            print(" Invalid command. Use 'n', 'p', or 'q'.")
