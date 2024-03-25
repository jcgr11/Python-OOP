class EnrollmentError(Exception):
    pass


class AlreadyEnrolledError(EnrollmentError):
    pass


class CapacityReachedError(EnrollmentError):
    pass


class StudentNotFoundError(EnrollmentError):
    pass
