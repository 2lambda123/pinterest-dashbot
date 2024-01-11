from instapy import InstaPy


class InstaUtils:
    def __init__(self, username, password, nogui=True):
        self.username = username
        self.password = password
        self.nogui = nogui

    def login(self):
        # Implement Instagram login logic here
        pass

    def set_do_follow(self, enabled, percentage, times):
        # Implement set_do_follow logic here
        pass

    def set_do_comment(self, enabled, percentage):
        # Implement set_do_comment logic here
        pass

    def set_comments(self, comments_pool):
        # Implement set_comments logic here
        pass

    def set_ignore_if_contains(self, ignore_words):
        # Implement set_ignore_if_contains logic here
        pass

    def like_by_tags(self, search_terms, amount):
        # Implement like_by_tags logic here
        pass

    def end(self):
        # Implement any necessary cleanup or final actions here
        pass
