"""initial migration

Revision ID: 7c913b9c9f0e
Revises:
Create Date: 2025-06-30 15:55:09.509518

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
import geoalchemy2
from sqlalchemy_searchable import sql_expressions

# revision identifiers, used by Alembic.
revision: str = "7c913b9c9f0e"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "asset",
        sa.Column("filename", sa.String(), nullable=True),
        sa.Column("storage_service", sa.String(), nullable=True),
        sa.Column("storage_path", sa.String(), nullable=True),
        sa.Column("mime_type", sa.String(), nullable=True),
        sa.Column("size", sa.Integer(), nullable=True),
        sa.Column(
            "search_vector",
            sqlalchemy_utils.types.ts_vector.TSVectorType(),
            nullable=True,
        ),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        "ix_asset_search_vector",
        "asset",
        ["search_vector"],
        unique=False,
        postgresql_using="gin",
    )
    op.create_table(
        "contact",
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("description", sa.String(length=255), nullable=True),
        sa.Column("email", sa.String(length=100), nullable=True),
        sa.Column("phone", sa.String(length=20), nullable=True),
        sa.Column(
            "search_vector",
            sqlalchemy_utils.types.ts_vector.TSVectorType(),
            nullable=True,
        ),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_index(
        "ix_contact_search_vector",
        "contact",
        ["search_vector"],
        unique=False,
        postgresql_using="gin",
    )
    op.create_table(
        "group",
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("description", sa.String(length=255), nullable=True),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "lexicon_category",
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("description", sa.String(length=255), nullable=True),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "lexicon_term",
        sa.Column("term", sa.String(length=100), nullable=False),
        sa.Column("definition", sa.String(length=255), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("term"),
    )
    op.create_table(
        "owner",
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("description", sa.String(length=255), nullable=True),
        sa.Column(
            "search_vector",
            sqlalchemy_utils.types.ts_vector.TSVectorType(),
            nullable=True,
        ),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_index(
        "ix_owner_search_vector",
        "owner",
        ["search_vector"],
        unique=False,
        postgresql_using="gin",
    )
    op.create_table(
        "pub_author",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("affiliation", sa.String(), nullable=True),
        sa.Column(
            "search_vector",
            sqlalchemy_utils.types.ts_vector.TSVectorType(),
            nullable=True,
        ),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        "ix_pub_author_search_vector",
        "pub_author",
        ["search_vector"],
        unique=False,
        postgresql_using="gin",
    )
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(length=255), nullable=False),
        sa.Column("password", sa.String(length=255), nullable=False),
        sa.Column("is_superuser", sa.Boolean(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("avatar_url", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "geochronology_age",
        sa.Column("location_id", sa.Integer(), nullable=False),
        sa.Column("age", sa.Float(), nullable=False),
        sa.Column("age_error", sa.Float(), nullable=True),
        sa.Column("method", sa.String(length=100), nullable=True),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["method"],
            ["lexicon_term.term"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "lexicon_term_category_association",
        sa.Column("lexicon_term", sa.String(length=100), nullable=False),
        sa.Column("category_name", sa.String(length=255), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["category_name"], ["lexicon_category.name"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(
            ["lexicon_term"], ["lexicon_term.term"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "lexicon_triple",
        sa.Column("subject", sa.String(length=100), nullable=False),
        sa.Column("predicate", sa.String(length=100), nullable=False),
        sa.Column("object_", sa.String(length=100), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.ForeignKeyConstraint(["object_"], ["lexicon_term.term"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["subject"], ["lexicon_term.term"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "owner_contact_association",
        sa.Column("owner_id", sa.Integer(), nullable=False),
        sa.Column("contact_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["contact_id"],
            ["contact.id"],
        ),
        sa.ForeignKeyConstraint(
            ["owner_id"],
            ["owner.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "pub_author_contact_association",
        sa.Column("author_id", sa.Integer(), nullable=False),
        sa.Column("contact_id", sa.Integer(), nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.ForeignKeyConstraint(["author_id"], ["pub_author.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["contact_id"], ["contact.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("author_id", "contact_id"),
    )
    op.create_table(
        "publication",
        sa.Column("title", sa.Text(), nullable=False),
        sa.Column("abstract", sa.Text(), nullable=True),
        sa.Column("doi", sa.String(), nullable=True),
        sa.Column("year", sa.Integer(), nullable=True),
        sa.Column("publisher", sa.String(), nullable=True),
        sa.Column("url", sa.String(), nullable=True),
        sa.Column("publication_type", sa.String(length=100), nullable=False),
        sa.Column(
            "search_vector",
            sqlalchemy_utils.types.ts_vector.TSVectorType(),
            nullable=True,
        ),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["publication_type"],
            ["lexicon_term.term"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("doi"),
    )
    op.create_index(
        "ix_publication_search_vector",
        "publication",
        ["search_vector"],
        unique=False,
        postgresql_using="gin",
    )
    op.create_table(
        "sample_location",
        sa.Column("name", sa.String(length=100), nullable=True),
        sa.Column("description", sa.String(length=255), nullable=True),
        sa.Column("visible", sa.Boolean(), nullable=False),
        sa.Column(
            "point",
            geoalchemy2.types.Geometry(
                geometry_type="POINT",
                srid=4326,
                from_text="ST_GeomFromEWKT",
                name="geometry",
                nullable=False,
            ),
            nullable=False,
        ),
        sa.Column("owner_id", sa.Integer(), nullable=True),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.ForeignKeyConstraint(["owner_id"], ["owner.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    # op.create_index('idx_sample_location_point', 'sample_location', ['point'], unique=False, postgresql_using='gist')
    op.create_table(
        "asset_location_association",
        sa.Column("asset_id", sa.Integer(), nullable=False),
        sa.Column("location_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.ForeignKeyConstraint(["asset_id"], ["asset.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(
            ["location_id"], ["sample_location.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "equipment",
        sa.Column("equipment_type", sa.String(length=50), nullable=True),
        sa.Column("model", sa.String(length=50), nullable=True),
        sa.Column("serial_no", sa.String(length=50), nullable=True),
        sa.Column("date_installed", sa.DateTime(), nullable=True),
        sa.Column("date_removed", sa.DateTime(), nullable=True),
        sa.Column("recording_interval", sa.Integer(), nullable=True),
        sa.Column("equipment_notes", sa.String(length=50), nullable=True),
        sa.Column("location_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["location_id"], ["sample_location.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "group_location_association",
        sa.Column("group_id", sa.Integer(), nullable=False),
        sa.Column("location_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.ForeignKeyConstraint(["group_id"], ["group.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(
            ["location_id"], ["sample_location.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "pub_author_publication_association",
        sa.Column("publication_id", sa.Integer(), nullable=False),
        sa.Column("author_id", sa.Integer(), nullable=False),
        sa.Column("author_order", sa.Integer(), nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.ForeignKeyConstraint(["author_id"], ["pub_author.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(
            ["publication_id"], ["publication.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("publication_id", "author_id"),
    )
    op.create_table(
        "spring",
        sa.Column("description", sa.String(length=255), nullable=True),
        sa.Column("location_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["location_id"], ["sample_location.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "well",
        sa.Column("location_id", sa.Integer(), nullable=False),
        sa.Column("ose_pod_id", sa.String(length=50), nullable=True),
        sa.Column("api_id", sa.String(length=50), nullable=True),
        sa.Column("usgs_id", sa.String(length=50), nullable=True),
        sa.Column("well_depth", sa.Float(), nullable=True),
        sa.Column("hole_depth", sa.Float(), nullable=True),
        sa.Column("well_type", sa.String(length=100), nullable=True),
        sa.Column("casing_diameter", sa.Float(), nullable=True),
        sa.Column("casing_depth", sa.Float(), nullable=True),
        sa.Column("casing_description", sa.String(length=50), nullable=True),
        sa.Column("construction_notes", sa.String(length=250), nullable=True),
        sa.Column("formation_zone", sa.String(length=100), nullable=True),
        sa.Column(
            "search_vector",
            sqlalchemy_utils.types.ts_vector.TSVectorType(),
            nullable=True,
        ),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["formation_zone"],
            ["lexicon_term.term"],
        ),
        sa.ForeignKeyConstraint(
            ["location_id"], ["sample_location.id"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(
            ["well_type"],
            ["lexicon_term.term"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        "ix_well_search_vector",
        "well",
        ["search_vector"],
        unique=False,
        postgresql_using="gin",
    )
    op.create_table(
        "collaborative_network_well",
        sa.Column("actively_monitored", sa.Boolean(), nullable=False),
        sa.Column("well_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.ForeignKeyConstraint(["well_id"], ["well.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "geothermal_sample_set",
        sa.Column("well_id", sa.Integer(), nullable=True),
        sa.Column("name", sa.String(length=128), nullable=True),
        sa.Column("klass", sa.String(length=24), nullable=True),
        sa.Column("type", sa.String(length=50), nullable=True),
        sa.Column("porosity", sa.Integer(), nullable=True),
        sa.Column("permeability", sa.Integer(), nullable=True),
        sa.Column("density", sa.Integer(), nullable=True),
        sa.Column("dst_tests", sa.Boolean(), nullable=True),
        sa.Column("thin_section", sa.Boolean(), nullable=True),
        sa.Column("geochron", sa.Boolean(), nullable=True),
        sa.Column("geochem", sa.Boolean(), nullable=True),
        sa.Column("geothermal", sa.Boolean(), nullable=True),
        sa.Column("wholerock", sa.Boolean(), nullable=True),
        sa.Column("paleontology", sa.Boolean(), nullable=True),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.ForeignKeyConstraint(["well_id"], ["well.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "geothermal_temperature_profile",
        sa.Column("well_id", sa.Integer(), nullable=True),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.ForeignKeyConstraint(["well_id"], ["well.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "water_chemistry_analysis_set",
        sa.Column("well_id", sa.Integer(), nullable=True),
        sa.Column("note", sa.String(length=255), nullable=True),
        sa.Column("collection_timestamp", sa.DateTime(), nullable=False),
        sa.Column("laboratory", sa.String(length=255), nullable=True),
        sa.Column("collection_method", sa.String(length=100), nullable=True),
        sa.Column("sample_type", sa.String(length=100), nullable=True),
        sa.Column("visible", sa.Boolean(), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["collection_method"],
            ["lexicon_term.term"],
        ),
        sa.ForeignKeyConstraint(
            ["sample_type"],
            ["lexicon_term.term"],
        ),
        sa.ForeignKeyConstraint(["well_id"], ["well.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "well_screen",
        sa.Column("well_id", sa.Integer(), nullable=False),
        sa.Column("screen_depth_top", sa.Float(), nullable=False),
        sa.Column("screen_depth_bottom", sa.Float(), nullable=False),
        sa.Column("screen_type", sa.String(length=100), nullable=True),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["screen_type"],
            ["lexicon_term.term"],
        ),
        sa.ForeignKeyConstraint(["well_id"], ["well.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "well_timeseries",
        sa.Column("well_id", sa.Integer(), nullable=False),
        sa.Column("equipment_id", sa.Integer(), nullable=True),
        sa.Column("name", sa.String(length=100), nullable=True),
        sa.Column("description", sa.String(length=255), nullable=True),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column(
            "properties",
            sa.JSON(),
            nullable=True,
            comment="JSONB column for storing additional properties",
        ),
        sa.ForeignKeyConstraint(
            ["equipment_id"], ["equipment.id"], ondelete="SET NULL"
        ),
        sa.ForeignKeyConstraint(["well_id"], ["well.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "geothermal_bottom_hole_temperature_header",
        sa.Column("sample_set_id", sa.Integer(), nullable=True),
        sa.Column("drill_fluid", sa.String(length=100), nullable=True),
        sa.Column("fluid_salinity", sa.Float(), nullable=True),
        sa.Column("fluid_resistivity", sa.Float(), nullable=True),
        sa.Column("fluid_ph", sa.Float(), nullable=True),
        sa.Column("fluid_level", sa.Float(), nullable=True),
        sa.Column("fluid_viscosity", sa.Float(), nullable=True),
        sa.Column("fluid_loss", sa.Float(), nullable=True),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["drill_fluid"],
            ["lexicon_term.term"],
        ),
        sa.ForeignKeyConstraint(
            ["sample_set_id"],
            ["geothermal_sample_set.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "geothermal_temperature_profile_observation",
        sa.Column("temperature_profile_id", sa.Integer(), nullable=True),
        sa.Column("depth", sa.Float(), nullable=True),
        sa.Column("depth_unit", sa.String(length=100), nullable=True),
        sa.Column("temperature", sa.Float(), nullable=True),
        sa.Column("temperature_unit", sa.String(length=100), nullable=True),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["depth_unit"],
            ["lexicon_term.term"],
        ),
        sa.ForeignKeyConstraint(
            ["temperature_profile_id"],
            ["geothermal_temperature_profile.id"],
        ),
        sa.ForeignKeyConstraint(
            ["temperature_unit"],
            ["lexicon_term.term"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "geothermal_well_interval",
        sa.Column("sample_set_id", sa.Integer(), nullable=True),
        sa.Column("top_depth", sa.Float(), nullable=True),
        sa.Column("bottom_depth", sa.Float(), nullable=True),
        sa.Column("depth_unit", sa.String(length=100), nullable=True),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["depth_unit"],
            ["lexicon_term.term"],
        ),
        sa.ForeignKeyConstraint(
            ["sample_set_id"],
            ["geothermal_sample_set.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "groundwater_level_observation",
        sa.Column("timestamp", sa.DateTime(), nullable=False),
        sa.Column("value", sa.Float(), nullable=False),
        sa.Column("unit", sa.String(), nullable=False),
        sa.Column("data_quality", sa.String(length=100), nullable=True),
        sa.Column("level_status", sa.String(length=100), nullable=True),
        sa.Column("timeseries_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column(
            "properties",
            sa.JSON(),
            nullable=True,
            comment="JSONB column for storing additional properties",
        ),
        sa.Column("quality_control_status", sa.String(length=100), nullable=True),
        sa.Column("quality_control_notes", sa.Text(), nullable=True),
        sa.Column("quality_control_timestamp", sa.DateTime(), nullable=True),
        sa.Column("quality_control_user_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["data_quality"],
            ["lexicon_term.term"],
        ),
        sa.ForeignKeyConstraint(
            ["level_status"],
            ["lexicon_term.term"],
        ),
        sa.ForeignKeyConstraint(
            ["quality_control_status"],
            ["lexicon_term.term"],
        ),
        sa.ForeignKeyConstraint(
            ["quality_control_user_id"], ["user.id"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(
            ["timeseries_id"], ["well_timeseries.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "water_chemistry_analysis",
        sa.Column("analysis_set_id", sa.Integer(), nullable=True),
        sa.Column("value", sa.Float(), nullable=True),
        sa.Column("unit", sa.String(length=100), nullable=True),
        sa.Column("uncertainty", sa.Float(), nullable=True),
        sa.Column("method", sa.String(length=100), nullable=True),
        sa.Column("analyte", sa.String(length=100), nullable=False),
        sa.Column("analysis_timestamp", sa.DateTime(), nullable=True),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["analysis_set_id"],
            ["water_chemistry_analysis_set.id"],
        ),
        sa.ForeignKeyConstraint(
            ["analyte"],
            ["lexicon_term.term"],
        ),
        sa.ForeignKeyConstraint(
            ["unit"],
            ["lexicon_term.term"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "geothermal_bottom_hole_temperature",
        sa.Column("header_id", sa.Integer(), nullable=True),
        sa.Column("depth", sa.Float(), nullable=True),
        sa.Column("depth_unit", sa.String(length=100), nullable=True),
        sa.Column("temperature", sa.Float(), nullable=True),
        sa.Column("temperature_unit", sa.String(length=100), nullable=True),
        sa.Column("hours_since_circulation", sa.Float(), nullable=True),
        sa.Column("date_measured", sa.DateTime(), nullable=True),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["depth_unit"],
            ["lexicon_term.term"],
        ),
        sa.ForeignKeyConstraint(
            ["header_id"],
            ["geothermal_bottom_hole_temperature_header.id"],
        ),
        sa.ForeignKeyConstraint(
            ["temperature_unit"],
            ["lexicon_term.term"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "geothermal_heat_flow",
        sa.Column("interval_id", sa.Integer(), nullable=True),
        sa.Column("gradient", sa.Float(), nullable=True),
        sa.Column("gradient_unit", sa.String(length=100), nullable=True),
        sa.Column("ka", sa.Float(), nullable=True),
        sa.Column("ka_unit", sa.String(length=100), nullable=True),
        sa.Column("kpr", sa.Float(), nullable=True),
        sa.Column("kpr_unit", sa.String(length=100), nullable=True),
        sa.Column("q", sa.Float(), nullable=True),
        sa.Column("q_unit", sa.String(length=100), nullable=True),
        sa.Column("pm", sa.Float(), nullable=True),
        sa.Column("pm_unit", sa.String(length=100), nullable=True),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["gradient_unit"],
            ["lexicon_term.term"],
        ),
        sa.ForeignKeyConstraint(
            ["interval_id"],
            ["geothermal_well_interval.id"],
        ),
        sa.ForeignKeyConstraint(
            ["ka_unit"],
            ["lexicon_term.term"],
        ),
        sa.ForeignKeyConstraint(
            ["kpr_unit"],
            ["lexicon_term.term"],
        ),
        sa.ForeignKeyConstraint(
            ["pm_unit"],
            ["lexicon_term.term"],
        ),
        sa.ForeignKeyConstraint(
            ["q_unit"],
            ["lexicon_term.term"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "geothermal_thermal_conductivity",
        sa.Column("interval_id", sa.Integer(), nullable=True),
        sa.Column("conductivity", sa.Float(), nullable=True),
        sa.Column("conductivity_unit", sa.String(length=100), nullable=True),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["conductivity_unit"],
            ["lexicon_term.term"],
        ),
        sa.ForeignKeyConstraint(
            ["interval_id"],
            ["geothermal_well_interval.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # op.drop_table('spatial_ref_sys')

    op.execute("CREATE EXTENSION IF NOT EXISTS postgis;")
    op.execute(sql_expressions.statement)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("DROP FUNCTION parse_websearch(regconfig, text);")
    op.execute("DROP FUNCTION parse_websearch(text);")

    op.drop_table("geothermal_thermal_conductivity")
    op.drop_table("geothermal_heat_flow")
    op.drop_table("geothermal_bottom_hole_temperature")
    op.drop_table("water_chemistry_analysis")
    op.drop_table("groundwater_level_observation")
    op.drop_table("geothermal_well_interval")
    op.drop_table("geothermal_temperature_profile_observation")
    op.drop_table("geothermal_bottom_hole_temperature_header")
    op.drop_table("well_timeseries")
    op.drop_table("well_screen")
    op.drop_table("water_chemistry_analysis_set")
    op.drop_table("geothermal_temperature_profile")
    op.drop_table("geothermal_sample_set")
    op.drop_table("collaborative_network_well")
    op.drop_index("ix_well_search_vector", table_name="well", postgresql_using="gin")
    op.drop_table("well")
    op.drop_table("spring")
    op.drop_table("pub_author_publication_association")
    op.drop_table("group_location_association")
    op.drop_table("equipment")
    op.drop_table("asset_location_association")
    op.drop_index(
        "idx_sample_location_point",
        table_name="sample_location",
        postgresql_using="gist",
    )
    op.drop_table("sample_location")
    op.drop_index(
        "ix_publication_search_vector", table_name="publication", postgresql_using="gin"
    )
    op.drop_table("publication")
    op.drop_table("pub_author_contact_association")
    op.drop_table("owner_contact_association")
    op.drop_table("lexicon_triple")
    op.drop_table("lexicon_term_category_association")
    op.drop_table("geochronology_age")
    op.drop_table("user")
    op.drop_index(
        "ix_pub_author_search_vector", table_name="pub_author", postgresql_using="gin"
    )
    op.drop_table("pub_author")
    op.drop_index("ix_owner_search_vector", table_name="owner", postgresql_using="gin")
    op.drop_table("owner")
    op.drop_table("lexicon_term")
    op.drop_table("lexicon_category")
    op.drop_table("group")
    op.drop_index(
        "ix_contact_search_vector", table_name="contact", postgresql_using="gin"
    )
    op.drop_table("contact")
    op.drop_index("ix_asset_search_vector", table_name="asset", postgresql_using="gin")
    op.drop_table("asset")
    # ### end Alembic commands ###
