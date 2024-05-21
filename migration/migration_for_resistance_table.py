from masoniteorm.migrations import Migration


class MigrationForResistanceTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("resistances") as table:
            table.increments("id").unique()
            table.float("value")
            table.text("type")
            table.timestamp("created_at")

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("resistances")