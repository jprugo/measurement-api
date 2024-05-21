from masoniteorm.migrations import Migration


class MigrationForVibrationTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("vibrations") as table:
            table.increments("id").unique()
            table.float("value")
            table.text("type")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("pressures")