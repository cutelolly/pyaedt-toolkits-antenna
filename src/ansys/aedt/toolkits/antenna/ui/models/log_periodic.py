import os

import requests

from ansys.aedt.toolkits.antenna.ui.common.logger_handler import logger


class LogPeriodic(object):
    """Manages UI log periodic antenna."""

    def __init__(self):
        self.antenna_template = None
        pass

    def draw_ldpa_ui(self):
        """Create an LDPA antenna."""
        if self.backend_busy():
            msg = "Toolkit running"
            logger.debug(msg)
            self.write_log_line(msg)
            return

        properties_request = requests.get(self.url + "/get_properties")
        properties = properties_request.json()
        if properties["antenna_created"]:
            msg = "Antenna is already created, please open the antenna wizard again to create a new antenna"
            logger.debug(msg)
            self.write_log_line(msg)
            return

        self.property_table.clear()
        self.property_table.setRowCount(0)

        # Update antenna type
        self.antenna_template = "LDPA"

        self._add_header("LDPA", "10")

        self._add_footer(self.get_antenna)

        # Add image
        image = self._add_image(os.path.join(self.images_path, "LogPeriodicArray.png"))
        self.image_layout.addLayout(image, 0, 0, 1, 1)

        msg = "Antenna not implemented"
        logger.debug(msg)
        self.write_log_line(msg)

    def draw_toothed_ui(self):
        """Create a log periodic toothed antenna."""
        if self.backend_busy():
            msg = "Toolkit running"
            logger.debug(msg)
            self.write_log_line(msg)
            return

        properties_request = requests.get(self.url + "/get_properties")
        properties = properties_request.json()
        if properties["antenna_created"]:
            msg = "Antenna is already created, please open the antenna wizard again to create a new antenna"
            logger.debug(msg)
            self.write_log_line(msg)
            return

        self.property_table.clear()
        self.property_table.setRowCount(0)

        # Update antenna type
        self.antenna_template = "Toothed"

        self._add_header("Toothed", "10")

        self._add_footer(self.get_antenna)

        # Add image
        image = self._add_image(os.path.join(self.images_path, "LogTooth.jpg"))
        self.image_layout.addLayout(image, 0, 0, 1, 1)

        msg = "Antenna not implemented"
        logger.debug(msg)
        self.write_log_line(msg)

    def draw_trapezoidal_ui(self):
        """Create a log periodic trapezoidal antenna."""
        if self.backend_busy():
            msg = "Toolkit running"
            logger.debug(msg)
            self.write_log_line(msg)
            return

        properties_request = requests.get(self.url + "/get_properties")
        properties = properties_request.json()
        if properties["antenna_created"]:
            msg = "Antenna is already created, please open the antenna wizard again to create a new antenna"
            logger.debug(msg)
            self.write_log_line(msg)
            return

        self.property_table.clear()
        self.property_table.setRowCount(0)

        # Update antenna type
        self.antenna_template = "Trapezoidal"

        self._add_header("Trapezoidal", "10")

        self._add_footer(self.get_antenna)

        # Add image
        image = self._add_image(os.path.join(self.images_path, "LogTrap.jpg"))
        self.image_layout.addLayout(image, 0, 0, 1, 1)

        msg = "Antenna not implemented"
        logger.debug(msg)
        self.write_log_line(msg)
