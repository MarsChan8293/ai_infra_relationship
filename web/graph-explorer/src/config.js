export const TYPE_COLORS = {
  person: "#4f82b2", company: "#b57852", project: "#5d916c", "project-collection": "#6f9f79",
  community: "#4f9a9c", school: "#8b73b7", university: "#8b73b7", "research-institution": "#9b7abd",
  "model-team": "#b06f91", "model-project": "#7e88be", "person-link": "#7f8793",
  "relationship-map": "#7f8793", index: "#8d949e", note: "#8d949e", other: "#8d949e",
};

export const TYPE_NAMES = {
  person: "人物", company: "公司", project: "项目", "project-collection": "项目集合", community: "社区",
  school: "高校", university: "高校", "research-institution": "研究机构", "model-team": "模型团队",
  "model-project": "模型项目", "person-link": "人物镜像", "relationship-map": "关系图", index: "索引",
  note: "笔记", other: "其他",
};

export const DEFAULT_HIDDEN_TYPES = new Set(["index", "note", "person-link", "relationship-map"]);
export const COMMUNITY_PRIORITY = new Map([
  ["community", 90], ["project", 86], ["model-project", 84], ["project-collection", 82], ["model-team", 80],
  ["company", 70], ["school", 66], ["university", 66], ["research-institution", 66], ["person", 50],
]);

export function hash01(value) {
  let hash = 2166136261;
  for (let i = 0; i < value.length; i += 1) {
    hash ^= value.charCodeAt(i);
    hash = Math.imul(hash, 16777619);
  }
  return (hash >>> 0) / 4294967295;
}

export function scoreNode(node = {}) {
  return (node.bridgeScore || 0) * 4 + (node.degree || 0) + (node.crossCategoryDegree || 0) * 2;
}

export function nodeSize(node = {}) {
  return Math.max(2.6, Math.min(13, 2.8 + Math.log2((node.degree || 0) + 1) * 1.1 + (node.bridgeScore || 0) * 0.24));
}

export function graphColor(node = {}) {
  return TYPE_COLORS[node.type] || TYPE_COLORS.other;
}

export function escapeHtml(value) {
  return String(value ?? "").replace(/[&<>"']/g, (char) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;",
  }[char]));
}
