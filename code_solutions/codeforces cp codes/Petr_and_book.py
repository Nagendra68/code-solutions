def find_days_to_finish_book(pages, daily_pages):
    day = 0
    while pages > 0:
        pages -= daily_pages[day]
        day = (day + 1) % 7
    return day if day != 0 else 7

if __name__ == "__main__":
    pages = int(input())
    daily_pages = list(map(int, input().split()))
    print(find_days_to_finish_book(pages, daily_pages))
    