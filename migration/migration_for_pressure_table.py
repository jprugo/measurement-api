from masoniteorm.migrations import Migration


class MigrationForPressureTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("pressures") as table:
            table.increments("id").unique()
            table.float("value")
            table.text("type")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("pressures")