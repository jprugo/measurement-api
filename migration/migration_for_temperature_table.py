from masoniteorm.migrations import Migration


class MigrationForTemperatureTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("temperatures") as table:
            table.increments("id").unique()
            table.float("value")
            table.text("type")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("temperatures")