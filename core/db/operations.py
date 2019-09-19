# -*- coding: utf-8 -*-
"""`config.db.operations` module.

Provides core app  DB operations.
"""


from django.db.migrations.operations.base import Operation


class CreateShardID(Operation):
    """Create a Unique id generator across all db tables to
    enable sharding in multi-tenant scenarios
    """

    reduces_to_sql = False

    # If this is False, Django will refuse to reverse past this operation.
    reversible = False

    def state_forwards(self, app_label, state):
        """
        The Operation should take the 'state' parameter (an instance of
        django.db.migrations.state.ProjectState) and mutate it to match
        any schema changes that have occurred.
        Args:
            app_label:
            state:

        Returns:

        """
        pass

    def database_forwards(self, app_label, schema_editor, from_state, to_state):
        """Create the actual postgresql UDF and sequence.
        """
        schema_editor.execute(
            """
            CREATE SEQUENCE global_id_seq;
            CREATE OR REPLACE FUNCTION public.id_generator(
                OUT result bigint)
                RETURNS bigint
                LANGUAGE 'plpgsql'

                COST 100
                VOLATILE 
            AS $BODY$

            DECLARE
              our_epoch bigint := 1314220021721;
              seq_id bigint;
              now_millis bigint;
              shard_id int := 1;
              BEGIN
                SELECT nextval('global_id_seq')%%1024 INTO seq_id;

                SELECT FLOOR(EXTRACT(EPOCH FROM clock_timestamp()) * 1000) INTO now_millis;
                result := (now_millis - our_epoch) << 23;
                result := result | (shard_id << 10);
                result := result | (seq_id);
              END;

            $BODY$;
            """
        )

    def database_backwards(self, app_label, schema_editor, from_state, to_state):
        """
        If reversible is True, this is called when the operation is reversed.
        Args:
            app_label:
            schema_editor:
            from_state:
            to_state:

        Returns:

        """
        pass

    def describe(self):
        """
        This is used to describe what the operation does in console output.
        Returns:
        """
        return "Operation for creating unique shard id generator for postgresql"
