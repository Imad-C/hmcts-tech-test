export interface TaskPayload {
  title: string;
  description?: string;
  status: string;
  due: string;
}

export interface Task {
  id: number;
  title: string;
  description?: string;
  status: string;
  due: string;
}
