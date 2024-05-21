from masoniteorm.migrations import Migration


class MigrationForIsolationTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("isolations") as table:
            table.increments("id").unique()
            table.float("value")
            table.timestamp("created_at")

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("isolations")