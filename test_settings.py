class DisableMigrations:
    def __contains__(self, item):
        print("Test_settings1")
        return True

    def __getitem__(self, item):
        print("Test_settings2")
        return "notmigrations"

MIGRATION_MODULES = DisableMigrations()
