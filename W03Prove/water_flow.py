#Import libraries

#Define universal constants
rho = 998.2                 #kg/m^3
g = 9.80665                 #m/s^2
mu = 0.0010016              #Pascal seconds

def water_column_height(tower_height, tank_height):
    """Function takes parameters of tower height and 
    tank height and returns the value of the water column
    height

    Parameters: tower_height, tank_height (not sure what units)

    Returns: water_column_height (unknown units)
    """
    return tower_height + 3*tank_height/4

def pressure_gain_from_water_height(height):
    """Function takes parameters of height and 
    returns the value of the water pressure

    Parameters: tower_height, tank_height (not sure what units)

    Returns: water_column_height (unknown units)
    """
    return rho*g*height/1000

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor,
                            fluid_velocity):
    """Function takes parameters of pipe diameter, length, the friction factor,
    and velocity of the fluid and returns the pressure lost in kPa.

    Parameters: pipe diameter, length, the friction factor,
    and velocity of the fluid

    Returns: pressure lost from pipe in kPa
    """
    return (-friction_factor*pipe_length*rho*fluid_velocity*
            fluid_velocity/(2000*pipe_diameter))

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """Function takes parameters of fluid velocity and number of fittings,
    and returns the pressure lost in kPa.
    """
    return (-0.04 * rho * fluid_velocity* fluid_velocity * quantity_fittings)/2000

def reynolds_number(hydraulic_diameter, fluid_velocity):
    """Calculates the reynolds number from the hydraulic diameter and
    the fluid velocity.
    """
    return (rho*hydraulic_diameter*fluid_velocity)/mu

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity,
                                      reynolds_number, smaller_diameter):
    k = (0.1+(50/reynolds_number))*(((larger_diameter/smaller_diameter)**4)-1)
    return (-k*rho*fluid_velocity*fluid_velocity)/2000

def kpa_to_psi(pressure):
    return pressure/6.895

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    pressure_kpa = pressure
    pressure_psi = kpa_to_psi(pressure_kpa)

    print(f"Pressure at house: {pressure_kpa:.1f} kilopascals or {pressure_psi:.1f} psi")


if __name__ == "__main__":
    main()
